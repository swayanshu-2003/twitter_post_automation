# Twitter Automation Project

## OVERVIEW
This project is a Python-based application designed to automate the generation, scheduling, and posting of Twitter content, including educational threads on data science/AI topics and humorous posts tailored to Indian tech culture. It integrates with a PostgreSQL database using SQLAlchemy for storing tweet data, utilizes the Google Gemini API for content generation, and employs Tweepy for posting to Twitter. The system supports scheduling posts in Indian Standard Time (IST) with predefined time slots and handles both single tweets and threaded content.

### Key Features
- **Content Generation**: Generates educational tweet threads and funny posts using the Gemini API.
- **Scheduling**: Automatically schedules posts based on IST time slots.
- **Database Management**: Stores tweet metadata (e.g., topic, content, scheduled time) in a PostgreSQL database.
- **Twitter Integration**: Posts content to Twitter, supporting threads via Tweepy.
- **Modularity**: Organized into modules for generation, database operations, and posting.

## Tech Stack
- **Python 3.8+**: Core programming language.
- **SQLAlchemy**: ORM for database interactions with PostgreSQL.
- **Psycopg2-binary**: PostgreSQL adapter for SQLAlchemy.
- **Alembic**: Database migration tool.
- **Google-genai**: Interface to the Gemini API for AI-generated content.
- **Tweepy**: Twitter API client for posting tweets.
- **Python-dotenv**: Loads environment variables from `.env` files.
- **Pytz**: Handles timezone conversions, especially for IST.
- **Uuid**: Generates unique identifiers for database records.
- **Nltk**: Natural language processing library (optional, not fully utilized yet).
- **Spacy**: Advanced NLP library (optional, not fully utilized yet).
- **Schedule**: Job scheduling library (optional, not fully utilized yet).

## Installation

### Prerequisites
- **Python 3.8+**
- **PostgreSQL** (or another SQLAlchemy-supported database)
- **pip** (Python package manager)
- **Git** (for cloning the repository)

### Steps
1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**
   Install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add the following:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   DB_URL=postgresql://user:password@localhost:5432/dbname
   X_API_KEY=your_twitter_api_key_here
   X_API_SECRET=your_twitter_api_secret_here
   X_ACCESS_TOKEN=your_twitter_access_token_here
   X_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret_here
   X_USERNAME=your_twitter_username_here
   ```
   - Replace placeholders (e.g., `your_gemini_api_key_here`) with actual values obtained as described below.
   - Ensure the `DB_URL` matches your PostgreSQL setup.

4. **Obtain API Keys**
   - **Gemini API Key**:
     1. Visit the [Google AI Studio](https://aistudio.google.com/) website.
     2. Sign in with a Google account.
     3. Navigate to the "API Keys" section and click "Create API Key".
     4. Copy the generated key and paste it into the `.env` file as `GEMINI_API_KEY`.
   - **Twitter (X) API Key**:
     1. Go to the [Twitter Developer Portal](https://developer.twitter.com/).
     2. Sign in or create a Twitter Developer account.
     3. Apply for a developer account if not already approved (may require a use case description).
     4. Create a new project and app under the portal.
     5. Under the app’s settings, generate:
        - `API Key` and `API Secret Key` (found in the "Keys and Tokens" section).
        - `Access Token` and `Access Token Secret` (also in "Keys and Tokens" after enabling read/write access).
     6. Copy these values into the `.env` file as `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`, and set `X_USERNAME` to your Twitter handle (without @).
   - Note: Twitter API access may require a paid tier for full functionality.

5. **Initialize the Database**
   - Ensure your PostgreSQL server is running.
   - Set up the database and tables using Alembic:
     ```bash
     alembic upgrade head
     ```
   - Update `alembic.ini` if necessary to point to your environment.

## Usage

### Running the Application
1. **Generate and Schedule Posts**
   - For funny posts:
     ```bash
     python scripts/run_post_generation.py
     ```
     This script generates 4 funny posts based on themes like "college," "office," or "mixed" and saves them to the `funny_posts` table.
   - For educational threads (optional, for testing):
     Uncomment the alternative import and function call in `run_post_generation.py` and run:
     ```bash
     python scripts/run_post_generation.py
     ```
     This generates data science/AI-related threads and saves them to the `tweet_posts` table.

2. **Publish Scheduled Posts**
   - For funny posts:
     ```bash
     python scripts/run_publish_tweet.py
     ```
     This script checks for due funny posts and publishes them to Twitter.
   - For educational threads (optional):
     Uncomment the alternative import and function call in `run_publish_tweet.py` and run:
     ```bash
     python scripts/run_publish_tweet.py
     ```
     This publishes scheduled educational threads.

3. **Scheduling**
   - Posts are scheduled using predefined IST time slots (9:00 AM, 12:30 PM, 4:00 PM, 7:30 PM) via the `crud.py` module.
   - Use the `scheduler.py` module (if implemented) to automate recurring checks.

### Example Workflow
- Generate funny posts and save them to the database.
- Wait for the scheduled time or manually trigger `run_publish_tweet.py` to post.
- Monitor the console for success/failure messages.

## File Structure
```
twitter-automation/
├── .env                  # Environment variables (e.g., API keys)
├── .gitignore            # Git ignore file
├── alembic.ini           # Alembic configuration
├── README.md             # Project documentation
├── requirements.txt      # Dependency list
├── main.py               # Main application entry point (if implemented)
├── app/
│   ├── __init__.py       # Package initializer
│   ├── config.py         # Configuration settings
│   ├── db/
│   │   ├── __init__.py   # Database package initializer
│   │   ├── database.py   # SQLAlchemy engine and session setup
│   │   ├── crud.py       # Database CRUD operations
│   │   ├── models.py     # SQLAlchemy models (TweetPost, FunnyPost)
│   ├── model/
│   │   ├── __init__.py   # Model package initializer
│   │   ├── generator.py  # Gemini API content generation
│   ├── post_engine/
│   │   ├── __init__.py   # Post engine package initializer
│   │   ├── formatter.py  # Text chunking for threads
│   │   ├── post_to_x.py  # Twitter posting logic
│   │   ├── publish.py    # Publish educational threads
│   │   ├── publish_funny_post.py  # Publish funny posts
│   │   ├── post_generator.py  # Generate educational threads
│   │   ├── funny_post_generator.py  # Generate funny posts
│   │   ├── topics_generator.py  # Generate tweet topics
│   ├── topics/
│   │   ├── __init__.py   # Topics package initializer
│   │   ├── topics.py     # Data science topics list
│   ├── twitter/
│   │   ├── __init__.py   # Twitter package initializer
│   │   ├── config.py     # Twitter-specific config (if needed)
│   │   ├── poster.py     # Twitter posting logic (if implemented)
│   │   ├── utils.py      # Utility functions (if implemented)
├── scripts/
│   ├── run_post_generation.py  # Script to generate posts
│   ├── run_publish_tweet.py    # Script to publish tweets
│   ├── temp.py                 # Temporary script (if needed)
├── alembic/
│   ├── env.py                 # Alembic environment script
│   ├── script.py.mako         # Migration script template
│   ├── versions/              # Migration history
├── .git/
│   └── ...                    # Git metadata
```

## Dependencies
- `python-dotenv`: Load environment variables from `.env`.
- `tweepy`: Twitter API client.
- `schedule`: Job scheduling (if used).
- `google-genai`: Gemini API integration.
- `sqlalchemy`: Database ORM.
- `psycopg2-binary`: PostgreSQL adapter for SQLAlchemy.
- `nltk`: Natural language processing (if used).
- `uuid`: Unique identifier generation.
- `alembic`: Database migration tool.
- `spacy`: Advanced NLP library (if used).
- `pytz`: Timezone handling.

Install via `pip install -r requirements.txt`.

## Configuration
- **Environment Variables**: Defined in `config.py` and loaded from `.env`.
- **Database**: Configured via `DB_URL` in `.env`. Ensure PostgreSQL is set up with the specified user, password, and database name.
- **Twitter API**: Requires `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`, and `X_USERNAME` in `.env`.

## Database Setup
- **Models**: Defined in `app/db/models.py` with two tables:
  - `tweet_posts`: For educational threads (includes `topic`, `subtopic`, `tweet_topic`, etc.).
  - `funny_posts`: For humorous posts (includes `topic`, `tweet_content`, etc.).
- **Migration**: Use Alembic to manage schema changes. Run `alembic upgrade head` after configuration.

## Function Documentation

### `app/db/database.py`
- **`create_engine(DB_URL)`**: Creates a SQLAlchemy engine using the database URL from `config.py`.
- **`sessionmaker(autocommit=False, autoflush=False, bind=engine)`**: Configures a session factory for database transactions.
- **`declarative_base()`**: Sets up the base class for declarative models.

### `app/db/models.py`
- **`ist_now()`**: Returns the current datetime in IST (Asia/Kolkata) using `pytz`.
- **`TweetPost(Base)`**: Defines the `tweet_posts` table with columns: `id` (UUID), `topic`, `subtopic`, `tweet_topic`, `tweet_content`, `scheduled_time`, `tweet_link`, `is_thread`, `created_at`, `posted_at`.
- **`FunnyPost(Base)`**: Defines the `funny_posts` table with columns: `id` (UUID), `topic`, `tweet_content`, `scheduled_time`, `tweet_link`, `created_at`, `posted_at`.

### `app/db/crud.py`
- **`save_generated_tweets_to_db(tweets)`**: Saves a list of tweet dictionaries to the `tweet_posts` table with scheduled times based on IST slots.
- **`save_generated_tweets_to_funny_posts(tweets)`**: Saves a list of tweet dictionaries to the `funny_posts` table with scheduled times based on IST slots.

### `app/model/generator.py`
- **`generate(prompt: str)`**: Uses the Gemini API to generate content based on the provided prompt and returns the text.

### `app/post_engine/formatter.py`
- **`intelligent_chunk(text, max_len=280)`**: Splits text into chunks of max 280 characters, preserving paragraphs and adding numbering (e.g., "1/3").

### `app/post_engine/post_to_x.py`
- **`post_thread_to_twitter(tweet_chunks)`**: Posts a list of text chunks as a Twitter thread using Tweepy, returning tweet IDs or None on failure.

### `app/post_engine/publish.py`
- **`fetch_post_and_publish()`**: Fetches an unposted, due `TweetPost`, chunks its content, posts it as a thread, and updates the database with the tweet URL and `posted_at`.

### `app/post_engine/publish_funny_post.py`
- **`fetch_post_and_publish()`**: Fetches an unposted, due `FunnyPost`, posts it to Twitter, and updates the database with the tweet URL and `posted_at`.

### `app/post_engine/post_generator.py`
- **`generate_post_content()`**: Generates educational tweet threads based on data science topics, saves them to `tweet_posts`, and includes a 3-minute delay between iterations.
- **`generate_tweet_prompt(topic, subtopic, tweet_topic)`**: Creates a prompt for the Gemini API to generate a 600-character thread with a given topic, subtopic, and headline.

### `app/post_engine/funny_post_generator.py`
- **`generate_funnly_post_content(n=4)`**: Generates `n` funny posts based on random themes ("college," "office," "mixed") and saves them to `funny_posts`.
- **`generate_funnly_post_prompt(topic)`**: Creates a prompt for the Gemini API to generate a funny post based on the specified theme.

### `app/post_engine/topics_generator.py`
- **`select_random_topic_and_subtopic()`**: Randomly selects a topic and subtopic from `DATA_SCIENCE_TOPICS`.
- **`generate_tweet_topic(n=1)`**: Generates `n` tweet topics based on random topic/subtopic pairs with a 3-minute delay between iterations.

### `app/topics/topics.py`
- **`DATA_SCIENCE_TOPICS`**: A list of dictionaries containing data science topics and subtopics for content generation.

### `app/config.py`
- **`load_dotenv()`**: Loads environment variables from `.env`.
- Variables: `GEMINI_API_KEY`, `DB_URL`, `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET`, `X_USERNAME` (accessed via `os.getenv`).

### `scripts/run_post_generation.py`
- **`run_post_generation_job()`**: Calls `generate_funnly_post_content` (or `generate_post_content` if uncommented) to generate posts.

### `scripts/run_publish_tweet.py`
- **`run_publish_job()`**: Calls `fetch_post_and_publish` from `publish_funny_post.py` (or `publish.py` if uncommented) to publish posts.

## Development Notes
- **Rate Limiting**: The Gemini API and Twitter API have rate limits. The code includes 3-minute delays (e.g., in `topics_generator.py`, `post_generator.py`) to comply with free-tier restrictions.
- **Threading**: Educational threads may exceed 280 characters and are chunked using `intelligent_chunk` in `formatter.py`.
- **Testing**: Use the commented alternative code in `run_post_generation.py` and `run_publish_tweet.py` for testing educational threads.
- **Error Handling**: Implemented in `crud.py`, `publish.py`, and `publish_funny_post.py` to manage database and API errors.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request on GitHub.

## License
This project is currently unlicensed. Consider adding a license (e.g., MIT, GPL) in `LICENSE` file if you plan to open-source it.
