from app.model.generator import generate
from app.post_engine.topics_generator import generate_tweet_topic
from app.db.crud import save_generated_tweets_to_db
import time

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
    Your goal is to explain the following concept like you're talking to a curious class 5 kid who loves tech but also wants to crack FAANG interviews one day . you may include storytelling that may be funny if possible but not mandatory

    - Topic: {topic}
    - Subtopic: {subtopic}
    - Headline: "{tweet_topic}"

    Now generate a detailed, well-formatted tweet **thread** that:
    - add the Headline ({tweet_topic}) on the top
    - Explains the concept in a fun, engaging way
    - Uses simple language and relatable examples
    - Breaks down complex ideas into digestible parts
    - Keeps it educational but informal and attention-grabbing
    - Format the content naturally supported for posting on X 
    - Use plain text formatting
    - markdowns and line breaks(\ n) are not allowed
    - real line breaks are allowed(Enter)
    - Starts with a hook or question
    - Uses lists (1, 2, 3...), bullet points, emojis, code (if needed)
    - Explains everything clearly
    - Ends with questions, tips, or fun facts to boost engagement
    - add Hashtags and links to relevant resources if possible

    Format output as markdown-style tweet(s). Output should be plain text and should not exceed 800 characters in total.
    """





# def generate_tweet_prompt(tweet_topic: str) -> str:
#     return f"""
# You are a professional technical educator, storyteller, and content strategist with over 10 years of experience.

# 🎯 Your goal:
# Generate a SINGLE tweet between 100 and 600 characters that explains a **software engineering or machine learning concept** based on the following tweet topic:

# 🧠 Tweet Topic: {tweet_topic}

# 📢 Style & Tone:
# - Make it engaging, funny, human-like
# - Explain it like you're teaching a 10-year-old
# - Should feel like a tweet you'd want to retweet or screenshot
# - Include real-world or humorous analogies/examples if possible
# - Keep it educational but informal and attention-grabbing
# - include storytelling elements to make it relatable(not compulsory, only where it fits)

# 💡 Content Guidelines:
# - Must be informative yet understandable
# - Avoid overly technical terms unless explained simply
# - You can make jokes, exaggerate, or ask rhetorical questions to boost fun

# 📐 Format Rules (very important):
# - Use line breaks between sentences
# - Use emoji where appropriate, but limited
# - Use bullets •, dashes –, or numbered lists for clarity
# - Punchy sentence per line
# - End with a cliffhanger, quote, tip, or funny punchline if possible

# 🚫 Avoid:
# - Dense paragraphs
# - Overuse of technical jargon (little use is fine)

# Output ONLY the final tweet text.
# """
