import importlib
from io import StringIO
import sys
import types
import unittest
from unittest.mock import MagicMock, call, patch


class TestCase(unittest.TestCase):
    task_name = 'task'

    def setUp(self):
        self.fake_api = MagicMock()

        fake_tweepy = types.ModuleType("tweepy")

        class FakeTooManyRequests(Exception):
            pass

        class FakeTweepyException(Exception):
            pass

        class FakeCursor:
            def __init__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs

            def items(self, *args, **kwargs):
                return iter([])

        fake_tweepy.OAuth1UserHandler = MagicMock(return_value=MagicMock())
        fake_tweepy.API = MagicMock(return_value=self.fake_api)
        fake_tweepy.Cursor = FakeCursor
        fake_tweepy.TooManyRequests = FakeTooManyRequests
        fake_tweepy.TweepyException = FakeTweepyException

        self.module_patcher = patch.dict(sys.modules, {'tweepy': fake_tweepy})
        self.module_patcher.start()
        self.addCleanup(self.module_patcher.stop)

        try:
            with patch('sys.stdout', new=StringIO()) as self.actualOutput:
                if self.task_name in sys.modules:
                    self.task = importlib.reload(sys.modules[self.task_name])
                else:
                    self.task = importlib.import_module(self.task_name)
        except NameError:
            pass
        except Exception as e:
            self.fail(
                "There was a problem while loading the solution – {0}. Check the solution for "
                "IDE-highlighted errors and warnings.".format(str(e))
            )

    def test_get_user_info(self):
        fake_user = MagicMock()
        fake_user.name = "Polina"
        fake_user.screen_name = "polina_dev"
        fake_user.followers_count = 42

        api = MagicMock()
        api.verify_credentials.return_value = fake_user

        result = self.task.get_user_info(api)

        self.assertEqual(
            ("Polina", "polina_dev", 42),
            result,
            msg="get_user_info(api) should return the user's name, screen name, and follower count."
        )
        api.verify_credentials.assert_called_once()

    def test_limit_handle(self):
        class FakeCursor:
            def __init__(self):
                self.values = iter([
                    self_task.tweepy.TooManyRequests(),
                    "first",
                    "second"
                ])

            def __next__(self):
                value = next(self.values)
                if isinstance(value, Exception):
                    raise value
                return value

        self_task = self.task

        with patch.object(self.task.time, 'sleep') as mock_sleep:
            result = list(self.task.limit_handle(FakeCursor()))

        self.assertEqual(
            ["first", "second"],
            result,
            msg="limit_handle(cursor) should keep yielding items and continue after a rate limit error."
        )
        mock_sleep.assert_called_once()

    def test_follow_matching_users(self):
        follower_1 = MagicMock()
        follower_1.name = "Alice"
        follower_1.id = 1

        follower_2 = MagicMock()
        follower_2.name = "Bob"
        follower_2.id = 2

        follower_3 = MagicMock()
        follower_3.name = "Alice"
        follower_3.id = 3

        class FakeCursor:
            def __init__(self, *args, **kwargs):
                pass

            def items(self):
                return iter([follower_1, follower_2, follower_3])

        api = MagicMock()

        with patch.object(self.task.tweepy, 'Cursor', FakeCursor):
            result = self.task.follow_matching_users(api, "Alice")

        self.assertEqual(
            ["Alice", "Alice"],
            result,
            msg="follow_matching_users(api, target_name) should return only the names of matching followers."
        )
        self.assertEqual(
            [call(user_id=1), call(user_id=3)],
            api.create_friendship.call_args_list,
            msg="follow_matching_users(api, target_name) should follow only users whose names match the target."
        )

    def test_like_tweets(self):
        tweet_1 = MagicMock()
        tweet_1.id = 101

        tweet_2 = MagicMock()
        tweet_2.id = 102

        tweet_3 = MagicMock()
        tweet_3.id = 103

        class FakeCursor:
            def __init__(self, *args, **kwargs):
                pass

            def items(self, number_of_tweets):
                return iter([tweet_1, tweet_2, tweet_3][:number_of_tweets])

        api = MagicMock()

        def create_favorite_side_effect(tweet_id):
            if tweet_id == 102:
                raise self.task.tweepy.TweepyException("API error")

        api.create_favorite.side_effect = create_favorite_side_effect

        with patch.object(self.task.tweepy, 'Cursor', FakeCursor):
            result = self.task.like_tweets(api, "python", 3)

        self.assertEqual(
            [101, 103],
            result,
            msg="like_tweets(api, search_query, number_of_tweets) should return only successfully liked tweet ids."
        )
        self.assertEqual(
            [call(101), call(102), call(103)],
            api.create_favorite.call_args_list,
            msg="like_tweets(api, search_query, number_of_tweets) should try to like every tweet returned by the cursor."
        )