# Tweet Script

## What You'll Learn

Build a Python script that interacts with the Twitter API using the tweepy library to automate social media tasks like following users and liking tweets.

## Concept Overview

Python can automate interactions with social media platforms through their APIs (Application Programming Interfaces). This exercise uses the Twitter API to demonstrate authentication with OAuth, making API calls, handling rate limits, and automating social media workflows.

Working with external APIs is a crucial skill for integrating services, automating tasks, and building applications that interact with web platforms. Understanding API authentication, rate limiting, and error handling prepares you for working with various web services.

## Key Concepts

### OAuth Authentication

APIs use OAuth to securely authenticate applications:

```python
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
```

### Making API Calls

Use library methods to interact with the API:

```python
# Get authenticated user info
user = api.me()
print(user.name)
print(user.followers_count)

# Search for tweets
for tweet in api.search(query='python'):
    print(tweet.text)
```

### Rate Limit Handling

APIs limit request frequency to prevent abuse:

```python
def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(900)  # Wait 15 minutes
```

### API Cursors

Cursors handle pagination for large result sets:

```python
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)
```

## Example

```python
import tweepy

# Authenticate
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)

# Get your profile
me = api.me()
print(f"Account: {me.screen_name}")
print(f"Followers: {me.followers_count}")

# Search and like tweets
search_term = "python programming"
for tweet in tweepy.Cursor(api.search, search_term).items(5):
    try:
        tweet.favorite()
        print(f"Liked: {tweet.text[:50]}...")
    except tweepy.TweepError as e:
        print(f"Error: {e}")

# Follow users
for user in tweepy.Cursor(api.search_users, "developers").items(3):
    try:
        user.follow()
        print(f"Followed: {user.screen_name}")
    except tweepy.TweepError as e:
        print(f"Error: {e}")
```

## Your Task

Explore how to interact with external APIs using Python. Study OAuth authentication, making API calls, handling rate limits and errors, and automating social media workflows. Understand how third-party libraries simplify API interaction and how to handle common challenges like pagination and rate limiting.

**Note:** This requires creating Twitter API credentials and installing tweepy (`pip install tweepy`). The concepts apply to many web APIs beyond Twitter.
