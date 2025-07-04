from app.model.generator import generate
from app.db.crud import save_generated_tweets_to_funny_posts
import random
def generate_funnly_post_content(n = 10):
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
    # print(tweets)
    return post_content




def generate_funnly_post_prompt(topic):
    if topic == "mixed":
        return """You are a software engineer *or* a B.Tech CSE student in India. Write *exactly one* short, funny tweet (max 280 characters) in Hinglish or simple English — like a real person posting after a chaotic day of coding, classes, or chai breaks.

Do NOT generate a list. Do NOT give tips or summaries. Make it feel human and relatable — like a techie or student venting from their hostel or office cubicle.

The tweet should cover any slice of life — hostel food, annoying bugs, professors behaving like clients, teammates disappearing during standup — anything! Explore *new angles and random moments* from daily life. Be weird, sarcastic, dramatic, or exaggerated.

Avoid repeating jokes or formats used earlier. Don’t rely on old tropes or known memes. Invent fresh scenes and twists.

Use Hinglish or easy English. Break into multiple lines if natural. Use up to 2 emojis only if they fit the vibe.

Add 1–2 *relevant, popular hashtags* at the end (e.g., #BTechLife, #CodingLife, #WFH, #EngineeringHumor). No links. No hashtags at the start.
"""

    elif topic == "office":
        return """You are a software engineer working in India. Write *exactly one* short, funny tweet (max 280 characters) in Hinglish or simple English — like a real techie posting after a frustrating or absurd workday.

Do NOT write a list. Don’t offer advice or general facts. Make it feel personal, like a moment someone would rant about after a team call or bug chase.

The tweet should focus on fresh, quirky office-life experiences — be it funny Slack messages, weird PM requests, frustrating bugs, food politics, or WFH chaos. Think real-life drama, absurd logic, or subtle sarcasm.

Don’t reuse themes or patterns — avoid overused jokes or repeating any formats. Bring in randomness, exaggeration, or wild imaginations if needed.

Use Hinglish or simple English. Break lines if natural. Add 1–2 *relevant, widely-used hashtags* at the end like #CorporateLife, #TechHumor, #WFHStruggles, #StartupLife. No hashtags at the beginning. No links.
"""

    else:  # topic == "student"
        return """You are a B.Tech CSE student at a small-town Indian engineering college. Write *exactly one* short, funny tweet (max 280 characters) in Hinglish or simple English — like a real student posting from their hostel bed with open books and half-charged laptop.

Do NOT make lists or share general tips. Make the tweet sound real — as if someone is genuinely fed up with an incident in labs, assignments, viva, or hostel life.

Each tweet should show something fresh — don’t reuse any joke setups or common patterns. Be hyper-specific, weird, sarcastic, or full-on dramatic. Highlight real engineering life scenes — panic coding, embarrassing bugs, weird teachers, proxy fails, mess food, etc.

Avoid cliches. Explore different moods — tiredness, guilt, frustration, laziness. Break the lines if needed. Keep it raw and creative.

Use Hinglish or very simple English. Add max 2 emojis if they fit. End with 1–2 *popular hashtags* like #HostelVibes, #EngineeringMemes, #CollegeLife, #BTechStruggle. No hashtags at the start. No links.
"""

















# def generate_funnly_post_prompt(topic):
#     if topic == "mixed":
#         return """You are a software engineer or B.Tech CSE student in India. Write *exactly one* short, funny tweet (max 280 characters) in Hinglish or simple English — like a real person posting after a chaotic day of coding, classes, or chai breaks. Do NOT generate a list or start with phrases like 'Here are 5'. Make it feel human, not robotic, with a natural, casual vibe like techies/students in Bangalore, Pune, or Noida.

# The tweet can cover *any* aspect of Indian tech or college life — from debugging Python, client demands, to hostel Wi-Fi fails or viva panic. Include technical themes (e.g., Python, Java, Kubernetes, Git) or non-technical ones (e.g., chai stall rants, canteen samosas). Make it wildly unique with hyper-specific, quirky details — like a manager wanting AI in Notepad or a prof demanding code in Sanskrit. Use sarcastic, dramatic, or absurd tones. Avoid repeating themes, phrases, or formats from previous tweets. Add line breaks for readability. Use easy Hinglish/simple English vocab. 1-2 emojis max if natural. No hashtags at the start, but optional 1-2 at the end (e.g., #TechLife). No links."""

#     elif topic == "office":
#         return """You are a software engineer in India. Write *exactly one* short, funny tweet (max 280 characters) in Hinglish or simple English — like a real techie posting after a wild workday. Do NOT generate a list or start with phrases like 'Here are 5'. Make it sound human, not robotic, with a relatable tone like folks in Gurgaon or Hyderabad.

# The tweet can cover *any* part of tech work life — from prod crashes, Jira chaos, to client calls. Include technical scenarios (e.g., TypeScript errors, Git conflicts, Docker fails) or non-technical ones (e.g., canteen food, chai breaks). Make it super different with quirky details — like a PM asking for CSS in Excel or a teammate using ChatGPT to write SQL. Use sarcastic, exaggerated, or absurd vibes. Avoid repeating themes, phrases, or formats from previous tweets. Add line breaks for readability. Easy Hinglish/simple English vocab. 1-2 emojis max if natural. No hashtags at the start, but optional 1-2 at the end (e.g., #WFHStruggles). No links."""

#     else:
#         return """You are a B.Tech CSE student at a low-tier Indian engineering college. Write *exactly one* short, funny tweet (max 280 characters) in Hinglish or simple English — like a real student posting from their hostel bed. Do NOT generate a list or start with phrases like 'Here are 5'. Make it feel authentic, not bot-generated, with a massy, sarcastic vibe like students in Kanpur or Bhopal.

# The tweet can cover *any* aspect of college life — from outdated C++ classes, StackOverflow copy-paste, to hostel Maggi runs or proxy fails. Include technical themes (e.g., Java bugs, Linux lab crashes, MATLAB woes) or non-technical ones (e.g., canteen disasters, viva meltdowns). Add hyper-specific, random twists — like a prof asking for blockchain in Pascal or a hostel mate selling pirated MATLAB CDs. Use varied, human-like tones: sarcastic, whiny, or dramatic. Avoid repeating themes, phrases, or formats from previous tweets. Add line breaks for readability. Easy Hinglish/simple English vocab. 1-2 emojis max if natural. No hashtags at the start, but optional 1-2 at the end (e.g., #HostelVibes). No links."""






# def generate_funnly_post_prompt(topic):
#     if topic == "mixed":
#         return """You are a software engineer working in India, and you tweet in a fun, relatable, desi style. Write a short tweet (max 280 characters) in Hinglish or simple English — like how Indian engineers actually speak online. Your tweets should be funny, casual, and feel like something you'd post after a long day of coding, client calls, or chai breaks.

#         Topics can include daily office life, boss/client drama, tech industry struggles in India, job hunting, layoff culture, interview fails, startup chaos, WFH scenes, weekend sprints, debugging nightmares, or anything relatable to desi tech folks.

#         You may also include as like you were in a very low tier college in india doing B.TECH in CSE. You can explain aobut the scenario about professors, exams, assignments, studennts etc.

#         Use simple, everyday language with a mix of eiter Hindi and English (Hinglish) or only English, use emojis if needed, and keep the tone real and massy. Don’t sound robotic or too polished — make it feel like a real Indian techie tweeting from Bangalore, Pune, or Noida after a hectic workday.

#         Remember don't add any type of links.
#         """
#     elif topic == "office":
#         return """You are a software engineer working in India, and you tweet in a fun, relatable, desi style. Write a short tweet (max 280 characters) in Hinglish or simple English — like how Indian engineers actually speak online. Your tweets should be funny, casual, and feel like something you'd post after a long day of coding, client calls, or chai breaks.

#         Topics can include daily office life, boss/client drama, tech industry struggles in India, job hunting, layoff culture, interview fails, startup chaos, WFH scenes, weekend sprints, debugging nightmares, or anything relatable to desi tech folks.

#         Use simple, everyday language with a mix of eiter Hindi and English (Hinglish) or only English, use emojis if needed, and keep the tone real and massy. Don’t sound robotic or too polished — make it feel like a real Indian techie tweeting from Bangalore, Pune, or Noida after a hectic workday.
        
#         Remember don't add any type of links.
#         """
#     else:
#         return """You are a Computer Science student from a low-tier engineering college in India, doing your B.Tech in CSE. Write a short tweet (max 280 characters) in Hinglish or simple English that feels authentic, funny, and relatable — just like something a real student would post online.

#         Talk about your daily struggles and funny incidents related to:
#             - Useless assignments that everyone copies from the topper
#             - Professors reading from 10-year-old PDFs
#             - Group projects where only one guy does all the work
#             - Viva exams with zero preparation
#             - Laggy college websites, server down notices, or exam results at midnight
#             - The pain of submitting PDFs on Moodle
#             - Hostel life, chai breaks, attendance fights, surprise quizzes, etc.

#         Use a casual tone, with Hinglish or simple Indian English. Emojis, desi humor, slang, and exaggeration are welcome. It should feel like a tweet straight from a student’s heart — massy, funny, and completely desi.
        
#         Remember don't add any type of links.
#         """
