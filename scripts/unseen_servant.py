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

if __name__ == '__main__':
    # add argparse to change what is turned on and off for the discord/reddit bot
    discordbot.start_discord_bot()


