import tweepy
import time

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Create a user authentication handler
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

# Create a Tweepy API client
api = tweepy.API(auth)

search = "zerotomastery"
numberOfTweets = 2

# Return basic information about the authenticated user
def get_user_info(api):
  user = api.verify_credentials()
  return user.name, user.screen_name, user.followers_count

# Yield items from a cursor and pause if rate limits are reached
def limit_handle(cursor):
  while True:
    try:
      yield next(cursor)
    except tweepy.TooManyRequests:
      time.sleep(1000)  # Wait before retrying after hitting the rate limit
    except StopIteration:
      break # Stop when there are no more items


# Return names of followers that match the target name
def follow_matching_users(api, target_name):
    followed = []
    # Use Tweepy Cursor with api.get_followers, call .items(), and pass the result to limit_handle
    for follower in limit_handle(tweepy.Cursor(api.get_followers).items()):
        if follower.name == target_name:
            api.create_friendship(user_id=follower.id) # Follow this matching user
            followed.append(follower.name) # Keep their name in the results list
    return followed


# Like tweets found by search and return their ids
def like_tweets(api, search_query, number_of_tweets):
    liked = []

    # Use Tweepy Cursor with search_tweets to find tweets that match search_query,
    # then use items to go through the number of tweets given in number_of_tweets, one tweet at a time
    for tweet in tweepy.Cursor(api.search_tweets, q=search_query).items(number_of_tweets):
        try:
            api.create_favorite(tweet.id) # Like the tweet
            liked.append(tweet.id) # Save its id
        except tweepy.TweepyException:
            pass
    return liked

# This block is not required to complete the exercise correctly; it only shows how to call
# the functions manually, and to run it, you would first need to fill in your API credentials above
def main():
    name, screen_name, followers_count = get_user_info(api)
    print(name)
    print(screen_name)
    print(followers_count)

    for name in follow_matching_users(api, 'username_here'):
        print(name)

    print(like_tweets(api, search, numberOfTweets))


if __name__ == '__main__':
    main()