#generic interfaces and objects for working with the subreddit
import credentials
import praw

class fusion_subreddit():
    def __init__(self, subreddit='FusionTest'):
        self.cred = credentials.read_credentials('reddit')
        self.connection = praw.Reddit(client_id=self.cred['reddit']['client_id'],
                         client_secret=self.cred['reddit']['client_secret'],
                         user_agent=self.cred['reddit']['user_agent'],
                         username=self.cred['reddit']['username'],
                         password=self.cred['reddit']['password'])
        self.subreddit = self.connection.subreddit(subreddit)

    def test_bot_authentication(self):
        me = self.connection.user.me()
        if me == self.cred['reddit']['username']:
            print('Authentication with reddit as {} successful.'.format(me))
        else:
            print('Authentication with reddit as {} failed.'.format(self.cred['reddit']['username']))

    def check_for_new_posts(self):
        for post in self.subreddit.new():
            print("Title: {}".format(post.title))
            print("Text: {}".format(post.selftext))
            print("Flair: {}".format(post.link_flair_text))
            print("Score: {}".format(post.score))
            print('-'*30)
