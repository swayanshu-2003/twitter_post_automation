from datetime import datetime, date, time
from app.db.database import SessionLocal
from app.db.models import TweetPost
import pytz

# Define IST timezone
IST = pytz.timezone("Asia/Kolkata")

# Define your preferred time slots in IST
TIME_SLOTS = [
    time(9, 0),    # 09:00 AM
    time(12, 30),  # 12:30 PM
    time(16, 0),   # 04:00 PM
    time(19, 30),  # 07:30 PM
]

def save_generated_tweets_to_db(tweets):
    db = SessionLocal()
    try:
        today = datetime.now(IST).date()  # Get current date in IST

        for i, tweet in enumerate(tweets):
            # Combine current date with time slot
            scheduled_naive = datetime.combine(today, TIME_SLOTS[i % len(TIME_SLOTS)])
            
            # Localize to IST (only if not already timezone-aware)
            if scheduled_naive.tzinfo is None:
                scheduled_time = IST.localize(scheduled_naive)
            else:
                scheduled_time = scheduled_naive.astimezone(IST)

            new_tweet = TweetPost(
                topic=tweet['topic'],
                subtopic=tweet['subtopic'],
                tweet_topic=tweet['tweet_topic'],
                tweet_content=tweet['tweet_content'],
                scheduled_time=scheduled_time
            )
            db.add(new_tweet)

        db.commit()
        print(f"✅ Saved {len(tweets)} tweets to the database with IST scheduled times.")
    
    except Exception as e:
        db.rollback()
        print(f"❌ Error saving tweets: {e}")
    
    finally:
        db.close()
