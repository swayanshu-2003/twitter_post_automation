from app.db.database import SessionLocal
from app.db.models import FunnyPost
# from app.post_engine.formatter import intelligent_chunk
from app.db.crud import delete_funny_post_by_id
from app.post_engine.post_to_x import post_thread_to_twitter
from app.config import X_USERNAME
import datetime
import pytz

def fetch_post_and_publish():
    db = SessionLocal()
    try:
        
        ist = pytz.timezone("Asia/Kolkata")
        now = datetime.datetime.now(ist)
        
        print(f"🕒 Now in IST: {now}")

        
        post: FunnyPost = db.query(FunnyPost)\
            .filter(
                FunnyPost.tweet_link.is_(None),
                FunnyPost.scheduled_time <= f"{now}"
            )\
            .order_by(FunnyPost.scheduled_time)\
            .first()

        if not post:
            print("⚠️ No unposted & due scheduled tweets found.")
            return

        print(f"🟡 Found post with ID: {post.id} scheduled for {post.scheduled_time} with text {post.tweet_content}")

        
        tweet_ids = post_thread_to_twitter([post.tweet_content])

        if not tweet_ids:
            print("❌ Posting failed.")
            delete_funny_post_by_id(post.id)
            return

        
        tweet_url = f"https://twitter.com/{X_USERNAME}/status/{tweet_ids[0]}"

       
        post.posted_at = datetime.datetime.now(ist)
        post.tweet_link = tweet_url
        db.commit()

        print(f"✅ Tweet posted and saved to DB: {tweet_url}")

    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()

    finally:
        db.close()

























