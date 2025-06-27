from datetime import datetime, date, time
from app.db.database import SessionLocal
from app.db.models import TweetPost,FunnyPost
import pytz

# Define IST timezone
IST = pytz.timezone("Asia/Kolkata")

# Define your preferred time slots in IST
from datetime import time

TIME_SLOTS = [
    time(2, 30),   # 08:00 AM IST
    time(4, 30),   # 10:00 AM IST
    time(7, 0),    # 12:30 PM IST
    time(8, 30),   # 02:00 PM IST
    time(10, 30),  # 04:00 PM IST
    time(12, 30),  # 06:00 PM IST
    time(14, 0),   # 07:30 PM IST
    time(15, 0),   # 08:30 PM IST
    time(16, 30),  # 10:00 PM IST
    time(17, 30),  # 11:00 PM IST
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
def save_generated_tweets_to_funny_posts(tweets):
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

            new_tweet = FunnyPost(
                topic=tweet['topic'],
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
