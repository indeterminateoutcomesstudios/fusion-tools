#top level script which instantiates all other parts
#glues together reddit, discord and database
import argparse
from database import Backend
import reddit

if __name__ == '__main__':
    be = Backend()
    print(be)
    if be.check_db():
        print('the database has tables')
    else:
        print('the database is empty')

    sr = reddit.fusion_subreddit()
    sr.test_bot_authentication()
    sr.check_for_new_posts()

    # starts the discord bot...need to probably run in subprocess?
    import discordbot


