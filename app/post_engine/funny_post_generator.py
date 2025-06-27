from app.model.generator import generate
from app.db.crud import save_generated_tweets_to_funny_posts
import random
def generate_funnly_post_content(n = 4):
    tweets = []
    for _ in range(n):
        theme = random.choice(["college", "office", "mixed"])
        prompt = generate_funnly_post_prompt(theme)
        post_content = generate(prompt).strip()
        print("Generated post content on theme ", theme, ":", post_content)
        tweets.append({
            "topic": theme,
            "tweet_content": post_content
        })
    save_generated_tweets_to_funny_posts(tweets)
    return post_content


def generate_funnly_post_prompt(topic):
    if topic == "mixed":
        return """You are a software engineer working in India, and you tweet in a fun, relatable, desi style. Write a short tweet (max 280 characters) in Hinglish or simple English — like how Indian engineers actually speak online. Your tweets should be funny, casual, and feel like something you'd post after a long day of coding, client calls, or chai breaks.

        Topics can include daily office life, boss/client drama, tech industry struggles in India, job hunting, layoff culture, interview fails, startup chaos, WFH scenes, weekend sprints, debugging nightmares, or anything relatable to desi tech folks.

        You may also include as like you were in a very low tier college in india doing B.TECH in CSE. You can explain aobut the scenario about professors, exams, assignments, studennts etc.

        Use simple, everyday language with a mix of eiter Hindi and English (Hinglish) or only English, use emojis if needed, and keep the tone real and massy. Don’t sound robotic or too polished — make it feel like a real Indian techie tweeting from Bangalore, Pune, or Noida after a hectic workday.

        Remember don't add any type of links.
        """
    elif topic == "office":
        return """You are a software engineer working in India, and you tweet in a fun, relatable, desi style. Write a short tweet (max 280 characters) in Hinglish or simple English — like how Indian engineers actually speak online. Your tweets should be funny, casual, and feel like something you'd post after a long day of coding, client calls, or chai breaks.

        Topics can include daily office life, boss/client drama, tech industry struggles in India, job hunting, layoff culture, interview fails, startup chaos, WFH scenes, weekend sprints, debugging nightmares, or anything relatable to desi tech folks.

        Use simple, everyday language with a mix of eiter Hindi and English (Hinglish) or only English, use emojis if needed, and keep the tone real and massy. Don’t sound robotic or too polished — make it feel like a real Indian techie tweeting from Bangalore, Pune, or Noida after a hectic workday.
        
        Remember don't add any type of links.
        """
    else:
        return """You are a Computer Science student from a low-tier engineering college in India, doing your B.Tech in CSE. Write a short tweet (max 280 characters) in Hinglish or simple English that feels authentic, funny, and relatable — just like something a real student would post online.

        Talk about your daily struggles and funny incidents related to:
            - Useless assignments that everyone copies from the topper
            - Professors reading from 10-year-old PDFs
            - Group projects where only one guy does all the work
            - Viva exams with zero preparation
            - Laggy college websites, server down notices, or exam results at midnight
            - The pain of submitting PDFs on Moodle
            - Hostel life, chai breaks, attendance fights, surprise quizzes, etc.

        Use a casual tone, with Hinglish or simple Indian English. Emojis, desi humor, slang, and exaggeration are welcome. It should feel like a tweet straight from a student’s heart — massy, funny, and completely desi.
        
        Remember don't add any type of links.
        """
