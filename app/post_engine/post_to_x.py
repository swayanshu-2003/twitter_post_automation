# import tweepy
# from app.config import X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET, X_API_KEY, X_API_SECRET

# def post_thread_to_twitter(tweet_chunks):
#     # Twitter API credentials
#     api_key = X_API_KEY
#     api_secret = X_API_SECRET
#     access_token = X_ACCESS_TOKEN
#     access_token_secret = X_ACCESS_TOKEN_SECRET

#     # Authenticate with Twitter using API v2
#     client = tweepy.Client(
#         consumer_key=api_key,
#         consumer_secret=api_secret,
#         access_token=access_token,
#         access_token_secret=access_token_secret
#     )

#     tweet_ids = []

#     try:
#         if not tweet_chunks:
#             print("❌ No tweet content provided.")
#             return None

#         # Post the first tweet
#         first_tweet = client.create_tweet(text=tweet_chunks[0])
#         tweet_ids.append(first_tweet.data['id'])
#         print(f"✅ First tweet posted: {first_tweet.data['id']}")

#         # If only one tweet, return
#         if len(tweet_chunks) == 1:
#             print("✅ Single tweet posted successfully!")
#             return tweet_ids

#         # Post rest as threaded replies
#         previous_tweet_id = first_tweet.data['id']
#         print(previous_tweet_id)
#         for chunk in tweet_chunks[1:]:
#             tweet = client.create_tweet(
#                 text=chunk,
#                 in_reply_to_tweet_id=previous_tweet_id
#             )
#             tweet_ids.append(tweet.data['id'])
#             previous_tweet_id = tweet.data['id']
#             print(f"✅ Reply tweet posted: {tweet.data['id']}")

#         print("✅ Thread posted successfully!")
#         return tweet_ids

#     except tweepy.TweepyException as e:
#         print(f"❌ Error posting tweet(s): {e}")
#         return None



import tweepy
from app.config import X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET, X_API_KEY, X_API_SECRET

def post_thread_to_twitter(tweet_chunks):
    # Credentials
    api_key = X_API_KEY
    api_secret = X_API_SECRET
    access_token = X_ACCESS_TOKEN
    access_token_secret = X_ACCESS_TOKEN_SECRET

    # Setup v2 client
    client_v2 = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Setup v1.1 client (for replies)
    auth_v1 = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api_v1 = tweepy.API(auth_v1)

    tweet_ids = []

    try:
        if not tweet_chunks:
            print("❌ No tweet content provided.")
            return None

        # Post the first tweet using v2
        first_tweet = client_v2.create_tweet(text=tweet_chunks[0])
        tweet_ids.append(first_tweet.data['id'])
        print(f"✅ First tweet posted: {first_tweet.data['id']}")

        # If only one tweet
        if len(tweet_chunks) == 1:
            print("✅ Single tweet posted successfully!")
            return tweet_ids

        # Replies using v1.1 API
        previous_tweet_id = first_tweet.data['id']
        for chunk in tweet_chunks[1:]:
            tweet = api_v1.update_status(status=chunk, in_reply_to_status_id=previous_tweet_id, auto_populate_reply_metadata=True)
            tweet_ids.append(tweet.id)
            previous_tweet_id = tweet.id
            print(f"✅ Reply tweet posted: {tweet.id}")

        print("✅ Thread posted successfully!")
        return tweet_ids

    except Exception as e:
        print(f"❌ Error posting tweet(s): {e}")
        return None
