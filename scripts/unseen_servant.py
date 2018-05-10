#top level script which instantiates all other parts
#glues together reddit, discord and database
#automated action to speed up DM metawork
#need backup (automated)
#fault tolerant
#interface with dicecloud?
# interface with vtt?
#send messages to DM when necessary
# voice channel scheduling for games/vtt
# music in IC tavern channel
# registering accounts [reddit & discord] (onboarding)
import argparse
import logging
logging.basicConfig(level=logging.INFO)
import discordbot # the discord bot actually is the master of the reddit bot, for simplicity

# import os
# import sys
# import psutil
# import logging

# def restart_program():
#     """Restarts the current program, with file objects and descriptors
#        cleanup
#     """

#     try:
#         p = psutil.Process(os.getpid())
#         for handler in p.get_open_files() + p.connections():
#             os.close(handler.fd)
#     except Exception, e:
#         logging.error(e)

#     python = sys.executable
#     os.execl(python, python, *sys.argv)


if __name__ == '__main__':
    # add argparse to change what is turned on and off for the discord/reddit bot
    discordbot.start_discord_bot()


