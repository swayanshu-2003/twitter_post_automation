from datetime import datetime, timedelta
from app.db.database import SessionLocal  # your SQLAlchemy DB session
from app.db.models import TweetPost      # your model
from datetime import datetime, timedelta, time

TIME_SLOTS = [
    time(9, 0),    # 09:00 AM
    time(12, 30),  # 12:30 PM
    time(16, 0),   # 04:00 PM
    time(19, 30),  # 07:30 PM
]


def save_generated_tweets_to_db(tweets):
    db = SessionLocal()
    today = datetime.now().date()
    

    for i,tweet in enumerate(tweets):
        schedule_time = datetime.combine(today, TIME_SLOTS[i % len(TIME_SLOTS)])

        
        new_tweet = TweetPost(
            topic=tweet['topic'],
            subtopic=tweet['subtopic'],
            tweet_topic=tweet['tweet_topic'],
            tweet_content=tweet['tweet_content'],
            scheduled_time=schedule_time
        )
        db.add(new_tweet)
    
    db.commit()
    db.close()
    print(f"Saved {len(tweets)} tweets to the database with scheduled times.")
