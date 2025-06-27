from app.model.generator import generate
from app.post_engine.topics_generator import generate_tweet_topic
from app.db.crud import save_generated_tweets_to_db
import time

# use the below code if you want to generate posts related to data science and AI topics covering in depth concepts, it generates a long text which can only be posted as a thread on X (formerly Twitter), but due to api restrcitions of free tier, it is not used in production, you can use it for testing purposes


def generate_post_content():
    tweets = []
    generated_topics = generate_tweet_topic(n=1)
    for i, topic in enumerate(generated_topics):
        tweet_topic = topic["tweet_topic"]
        prompt = generate_tweet_prompt(topic['topic'], topic['subtopic'], tweet_topic)
        tweet_content = generate(prompt).strip()
        tweets.append({
            "topic": topic['topic'],
            "subtopic": topic['subtopic'],
            "tweet_topic": tweet_topic,
            "tweet_content": tweet_content
        })
        
        if i < len(generated_topics) - 1:
            print("Waiting for 3 minutes before next iteration...")
            time.sleep(1 * 60)  # 3 minutes delay
        
    print("generated posts",tweets)
    save_generated_tweets_to_db(tweets)
    return tweets

def generate_tweet_prompt(topic,subtopic,tweet_topic) -> str:
    return f"""
    You are a 10+ year experienced technical educator, LLM prompt engineer, and viral tech content creator on X (formerly Twitter).

    You create educational  tweet **threads** that explain difficult software/data science/ML/AI concepts to developers in a clear, funny, and practical way using:
    - Humor & analogies
    - Real-world relatable examples
    - Step-by-step breakdowns
    - Interview-style questions
    - Lists, and emojis included
    - Easier vocabulary
    - Indian style of teaching
    - Storytelling elements to make it relatableif and only if its relevant
    Your goal is to explain the following concept like you're talking to a curious class 5 kid who loves tech but also wants to crack interviews one day . you may include storytelling that may be funny if possible but not mandatory

    - Topic: {topic}
    - Subtopic: {subtopic}
    - Headline: "{tweet_topic}"

    Now generate a detailed, well-formatted tweet **thread** that:
    - add the Headline ({tweet_topic}) on the top
    - Format the content naturally supported for posting on X 
    - Use plain text formatting
    - markdowns and line breaks(\ n) are not allowed
    - real line breaks are allowed(Enter)
    - Starts with a hook or question
    - Uses lists (1, 2, 3...), bullet points, emojis, code (if needed)
    - Ends with questions, tips, or fun facts to boost engagement
    - add Hashtags and links to relevant resources if possible

    Format output as markdown-style tweet(s). Output should be plain text and should be exactly of 600 characters in total.
    """



