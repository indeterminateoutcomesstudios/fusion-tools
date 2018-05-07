#generic interfaces and objects for working with the subreddit
import credentials
import praw

# will probably need to use something to continually monitor the stream of comments/posts
# http://praw.readthedocs.io/en/latest/tutorials/reply_bot.html

# register account with players/PCs
# add player accounts to subreddit

# check for new posts
# if post is a flair(write up), associate it with player and pc in backend
#   award tokens for submitting a write-up (with DM approval needed)
# if post is a flair(request),  notify DM of new request via discord
#   "I shall summon my master!"
# if post is a flair(map), associate it with player and pc in backend, as well as latest
#   award tokens? sticky the latest?
# search for keywords indicating player has voted on the map or write-up
#   transfer of tokens, confirm action with player on Discord, make record via subreddit post
# if the post is a flair(request) -> flair(succeeded), give all participating players +5 player tokens
# if the post is a flair(map), upload attachment to google drive for archive purposes

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
        print('-'*30)
        for post in self.subreddit.new():
            print("ID: {}".format(post))
            print("Title: {}".format(post.title))
            print("Text: {}".format(post.selftext))
            print("Flair: {}".format(post.link_flair_text))
            print("Score: {}".format(post.score))
            print('-'*30)

