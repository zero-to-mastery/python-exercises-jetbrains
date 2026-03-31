This exercise practices working with the `tweepy` module and the Twitter/X API.

`Tweepy` is a Python library for working with the Twitter/X API. It lets you authenticate as a user, request information from the API, and perform actions such as getting followers, searching for tweets, following users, and liking tweets through Python objects and methods instead of writing raw HTTP requests yourself. This exercise uses the `API` interface for Twitter API v1.1 together with `Cursor`, which helps work with paginated results. 

This exercise uses a Tweepy `API` style that is still supported and commonly used in learning materials. In [modern Tweepy documentation](https://docs.tweepy.org/), you will also see `Client` for Twitter API v2, but this task focuses on the `API` interface and OAuth 1.0a user authentication. 

### Authentication and API setup
In the beginning, we need to authenticate to work with the Twitter/X API. Usually, this is done with user credentials such as a `consumer key`, `consumer secret`, `access token`, and `access token secret`. In this exercise, however, you do not need to enter real credentials because the tests will provide artificial values. 

Still, the file includes a `main` section that calls all functions, so if you want, you can enter your own credentials and try running the file yourself.

- `OAuth1UserHandler`
Creates the authentication handler for OAuth 1.0a user context. It uses your consumer key, consumer secret, access token, and access token secret so Tweepy can make requests on behalf of the authenticated user. 

- `API(auth)`
Creates the Tweepy API client for Twitter API v1.1. 
After that, you can call methods such as `verify_credentials`, `get_followers`, `search_tweets`, `create_friendship`, and `create_favorite`.

- `api.verify_credentials()`
Returns information about the authenticated user. In this exercise, it is used to access values such as the user’s name, screen name, and follower count. Tweepy’s examples use this method to confirm that authentication works. 

### Working with followers and tweets
After authentication, the main part of the exercise is working with Twitter/X data and actions. These methods are used to read follower information, search for tweets, follow users, and like tweets.

- `api.get_followers`
Returns followers of a user through the API v1.1 followers endpoint. Because follower results can be long, this method is commonly used together with `Cursor` to process results page by page. 

- `api.search_tweets`
Searches for tweets that match a given query. In this task, the query is passed through `search_query`, and the results are iterated through with `Cursor`. 

- `api.create_friendship(...)`
Follows a user through the API. In this exercise, it is used when a follower’s name matches the target value. 

- `api.create_favorite(...)`
Likes a tweet through the API. In this exercise, it is used to like tweets returned by tweet search. 

### Pagination, iteration, and error handling
To work with longer API results, the exercise also uses helper tools for pagination, iteration, and exception handling. These make it easier to process many results one by one and continue working even if rate limits are reached.

- `Cursor(...)`
`Cursor` is Tweepy’s helper for pagination. Twitter/X API endpoints often return results in pages rather than all at once. `Cursor` hides that pagination logic and lets you move through the results one item at a time. You do not import it separately here because it is a class inside the `tweepy` module, so it is accessed as `tweepy.Cursor(...)`. 

- `items(...)`
`items` is used together with `Cursor` to iterate through results one by one. In this exercise, it is used both for follower results and for a limited number of tweet search results. 

- `TooManyRequests`
This exception is raised when the API rate limit is exceeded. In this task, it is caught inside `limit_handle`, which waits and then continues processing cursor results. 

- `TweepyException`
This is Tweepy’s general exception class. In this exercise, it is used to catch API-related errors that may happen while liking tweets. 

- `yield`
turns a function into a generator. Instead of returning all values at once, a generator produces them one at a time. In `limit_handle`, `yield` is used to return cursor results one by one while still allowing the function to pause and recover if a rate limit error happens. This is why `limit_handle` can wrap cursor iteration cleanly. 
