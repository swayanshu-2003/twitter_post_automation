# app/db/models.py
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base  # Assuming Base is from declarative_base()
# from sqlalchemy.dialects.postgresql import UUID
import uuid

class TweetPost(Base):
    __tablename__ = "tweet_posts"
    
    id = Column(String, primary_key=True, default=uuid.uuid4)
    topic = Column(String, nullable=False)
    subtopic = Column(String, nullable=False)
    tweet_topic = Column(String, nullable=False)
    tweet_content = Column(String)  # For actual tweet text later
    scheduled_time = Column(DateTime, default=None)
    tweet_link = Column(String, default=None)
    is_thread = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    posted_at = Column(DateTime, default=None)
