import praw
from secrets import Secrets

class Reddit():


    _my_client_id = 'RJU0Gi10B4FtCw'
    _my_client_secret = 'gX733gRRV_g-7T55kzNc4ItWsl0'
    _platform = 'web'
    _app_ID = 'com.bagosocks.redditSandbox'
    _version_string = 'v0.0.1'
    _user_string = '(by /u/hknecht)'
    _my_user_agent = "{}:{}:{} {}". \
        format(_platform, _app_ID, _version_string, _user_string)
    _secret = Secrets()

    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def open_reddit_read(self):
        self._reddit = praw.Reddit(client_id=self._my_client_id,
                         client_secret=self._my_client_secret,
                         user_agent=self._my_user_agent)

    def open_reddit_write(self):
        self._reddit = praw.Reddit(client_id=self._my_client_id,
                         client_secret=self._my_client_secret,
                         user_agent=self._my_user_agent,
                         username=self._secret.get_username(),
                         password=self._secret.get_password())


    def is_read_only(self):
        return self._reddit.read_only

    def top_submissions(self, subreddit, sub_limit):
        return self._reddit.subreddit(subreddit).hot(limit=sub_limit)