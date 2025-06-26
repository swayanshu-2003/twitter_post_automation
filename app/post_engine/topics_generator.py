import random

from app.topics.topics import DATA_SCIENCE_TOPICS
from app.model.generator import generate

import time

def select_random_topic_and_subtopic():
    selected_topic = random.choice(DATA_SCIENCE_TOPICS)
    topic_name = selected_topic["topic"]
    subtopic_name = random.choice(selected_topic["subtopics"])
    
    return {
        "topic": topic_name,
        "subtopic": subtopic_name
    }
    
def generate_tweet_topic(n=1):
    
    generated_topics = []
    for i in range(n):
        topic_info = select_random_topic_and_subtopic()
        topic = topic_info["topic"]
        subtopic = topic_info["subtopic"]
        base_prompt = f"""
            You are a professional technical content strategist and writer with over 10 years of experience .

            Your task is to generate a **modern, impactful, one-line tweet topic** that is:
            - Based on the following:
                - Topic: {topic}
                - Subtopic: {subtopic}
            - maximum 50 to 70 characters long
            - Relevant to today's developers and learners
            - High-retention and shareable

            Do NOT generate the tweet itself. Just return a powerful tweet **topic** or **headline** in 1 sentence that could be used to start a tweet or thread.

            Output Format: A single line only."""
        
        res = generate(base_prompt)
        generated_topics.append({
            id: i,
            "topic": topic,
            "subtopic": subtopic,
            "tweet_topic": res.strip()
        })
        
        if i < n - 1:
            print("Waiting for 3 minutes before next iteration...")
            time.sleep(1 * 60)  # 3 minutes delay
        
    print("generated topics",generated_topics)
    return generated_topics
   
    
    
    
    
    
    
    
    
    
