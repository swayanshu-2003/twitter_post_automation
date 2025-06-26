import requests
from app.config import X_BEARER_TOKEN

HEADERS = {
    "Authorization": f"Bearer {X_BEARER_TOKEN}",
    "Content-Type": "application/json"
}

def post_single_tweet(content: str):
    url = "https://api.twitter.com/2/tweets"
    response = requests.post(url, headers=HEADERS, json={"text": content})
    return response.json()

def post_thread(thread: list):
    tweet_ids = []
    reply_to = None
    for tweet in thread:
        payload = {"text": tweet}
        if reply_to:
            payload["reply"] = {"in_reply_to_tweet_id": reply_to}
        res = requests.post("https://api.twitter.com/2/tweets", headers=HEADERS, json=payload)
        data = res.json()
        tweet_ids.append(data["data"]["id"])
        reply_to = data["data"]["id"]
    return tweet_ids
