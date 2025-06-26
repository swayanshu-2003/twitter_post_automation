# 🚀 AI-Powered Tweet Scheduler

A fully automated pipeline that:
- ✅ Generates tweet threads daily at **midnight IST**
- 📅 Schedules them for **specific time slots** (9 AM, 12:30 PM, 4 PM, 7:30 PM)
- 🐦 Posts them directly to **Twitter (X)** as **threads**
- 💾 Stores and tracks each tweet in a **PostgreSQL** database
- 🛠️ Runs via **Render Cron Jobs** for serverless automation

---

## 🧩 Tech Stack

| Component        | Tech Used                     |
|------------------|-------------------------------|
| Backend          | FastAPI                       |
| Twitter API      | Tweepy + X (Twitter) API v2   |
| Scheduler        | Render Cron Jobs              |
| Database         | PostgreSQL (with SQLAlchemy)  |
| Deployment       | Render                        |

---

## 📁 Project Structure

```
project-root/
│
├── app/
│   ├── db/
│   │   ├── database.py        # SQLAlchemy DB setup
│   │   └── models.py          # TweetPost model
│   ├── post_engine/
│   │   ├── post_to_x.py       # Twitter API logic
│   │   ├── formatter.py       # Intelligent tweet chunker
│   │   └── scheduler.py       # Scheduled posting logic
│   └── main.py                # FastAPI entrypoint (optional UI/API)
│
├── cron/
│   ├── generate_posts.py      # Called daily at 12AM
│   └── scheduled_post.py      # Called every 5 mins to check & post
│
├── .env                       # Secrets (not committed)
├── requirements.txt
└── README.md
```

---

## 🛠️ Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-tweet-scheduler.git
cd ai-tweet-scheduler
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # For Linux/macOS
venv\Scripts\activate.bat    # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add:

```env
X_API_KEY=your_twitter_api_key
X_API_SECRET=your_twitter_api_secret
X_ACCESS_TOKEN=your_access_token
X_ACCESS_TOKEN_SECRET=your_access_token_secret
X_USERNAME=your_twitter_username

DATABASE_URL=postgresql://username:password@host:port/dbname
```

> 💡 Use a tool like [Render PostgreSQL](https://render.com/docs/databases) or local Postgres setup.

### 5. Run the App (Optional FastAPI Server)

```bash
uvicorn app.main:app --reload
```

---

## 🧠 Scheduled Jobs Setup (Render)

### 🕛 Midnight Post Generator

Runs at `00:00 IST` daily to generate tweet content.

```cron
0 18 * * *    # UTC time = 12 AM IST
```

Command:

```bash
python cron/generate_posts.py
```

### ⏰ Tweet Publisher (every 5 mins)

Checks database for scheduled tweets and posts them if due.

```cron
*/5 * * * *   # Every 5 mins
```

Command:

```bash
python cron/scheduled_post.py
```

---

## ✅ Features

- ✅ Intelligent Tweet Chunking (keeps threads clean & readable)
- 🧠 Modular Tweet Generators (add new topics easily)
- 🇮🇳 Full IST-based Scheduling
- 🌐 Render Compatible Cron Jobs
- 📡 Tweets are posted as real threads using Twitter API v2

---

## 🔐 Notes on API Access

Ensure your Twitter/X Developer App has:
- **Write permissions**
- **Elevated access** if you're hitting `403 Forbidden` for threads  
  ➤ [Apply for Elevated Access](https://developer.x.com/en/portal/products/elevated)

---

## 🤝 Contributing

Pull requests are welcome. Please open issues for feature requests, bug reports, or enhancements.

---

## 📄 License

MIT License. Use freely with attribution.