from app.db.database import SessionLocal
from app.db.models import TweetPost
from app.post_engine.formatter import intelligent_chunk
from app.post_engine.post_to_x import post_thread_to_twitter
from app.config import X_USERNAME
import datetime
import pytz

def fetch_post_and_publish():
    db = SessionLocal()

    try:
        # 1. Get current UTC time
        # now = datetime.datetime.utcnow()

        ist = pytz.timezone("Asia/Kolkata")
        now = datetime.datetime.now(ist)
        
        print(f"🕒 Now in IST: {now}")

        # 2. Fetch first unposted & due (scheduled_time <= now) tweet
        post: TweetPost = db.query(TweetPost)\
            .filter(
                TweetPost.tweet_link.is_(None),
                TweetPost.scheduled_time <= f"{now}"
            )\
            .order_by(TweetPost.scheduled_time)\
            .first()

        if not post:
            print("⚠️ No unposted & due scheduled tweets found.")
            return

        print(f"🟡 Found post with ID: {post.id} scheduled for {post.scheduled_time}")

        # 3. Chunk content
        tweet_chunks = intelligent_chunk(post.tweet_content)

        # 4. Post to Twitter
        tweet_ids = post_thread_to_twitter(tweet_chunks)

        if not tweet_ids:
            print("❌ Posting failed.")
            return

        # 5. Construct tweet URL from first tweet ID
        tweet_url = f"https://twitter.com/{X_USERNAME}/status/{tweet_ids[0]}"

        # 6. Update DB
        post.posted_at = datetime.datetime.now(ist)
        post.tweet_link = tweet_url
        post.is_thread = 1 if len(tweet_ids) > 1 else 0
        db.commit()

        print(f"✅ Tweet posted and saved to DB: {tweet_url}")

    except Exception as e:
        print(f"❌ Error: {e}")
        db.rollback()

    finally:
        db.close()



























# from app.db.database import SessionLocal
# from app.db.models import TweetPost
# from app.post_engine.formatter import intelligent_chunk
# from app.post_engine.post_to_x import post_thread_to_twitter
# from app.config import X_USERNAME
# import datetime

# def fetch_post_and_publish():
#     db = SessionLocal()

#     try:
#         # 1. Fetch one unposted tweet
#         post: TweetPost = db.query(TweetPost).filter_by(tweet_link=None).first()

#         if not post:
#             print("⚠️ No unposted tweets found.")
#             return

#         print(f"🟡 Found post with ID: {post.id}")

#         # 2. Chunk the content
#         tweet_chunks = intelligent_chunk(post.tweet_content)

#         # 3. Post to Twitter
#         tweet_ids = post_thread_to_twitter(tweet_chunks)

#         if not tweet_ids:
#             print("❌ Posting failed.")
#             return

#         # 4. Construct tweet URL (from first tweet ID)
#         tweet_url = f"https://twitter.com/{X_USERNAME}/status/{tweet_ids[0]}"

#         # 5. Update database
#         post.posted_at = datetime.datetime.now()
#         post.tweet_link = tweet_url
#         post.is_thread = 1 if len(tweet_ids) > 1 else 0
#         db.commit()

#         print(f"✅ Tweet posted and saved to DB: {tweet_url}")

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         db.rollback()

#     finally:
#         db.close()
