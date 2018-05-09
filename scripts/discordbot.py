#generic interfaces and definitions for handling discord interactions
import credentials
import discord
from discord.ext import commands
import asyncio
import logging
discord_log = logging.getLogger('discord')
import pprint
from database import Backend, db_log
from reddit import fusion_subreddit, reddit_log

# create database connection
db_log.info('Starting connection')
db = Backend()
if db.check_db():
    db_log.info('Tables are present, assuming they are correct')
else:
    db_log.info('The database is empty, reinitializing')
    db.destroy_db()
    db.initialize_db()

# create reddit connection
reddit_log.info('Starting connection')
sr = fusion_subreddit()
sr.test_bot_authentication()

cred = credentials.read_credentials('discord')
bot = commands.Bot(command_prefix='$')

def start_discord_bot():
    bot.run(cred['discord']['bot_token'])

async def check_subreddit(channel_id):
    await bot.wait_until_ready()
    channel = discord.Object(id=channel_id)
    while not bot.is_closed:
        # await bot.send_message(channel, "I'm alive!")
        discord_log.info('Checking subreddit for new posts.')
        sr.check_for_new_posts()
        await asyncio.sleep(30)

@bot.event
async def on_ready():
    discord_log.info('Logged in as')
    discord_log.info(bot.user.name)
    discord_log.info(bot.user.id)
    discord_log.info('------')
    for server in bot.servers:
        # discord_log.info("Server: {}".format(server.name))
        for channel in server.channels:
            # discord_log.info("  {} {} {}".format(channel.name, channel.type, channel.id))
            if str(channel.type) == 'text' and channel.name == 'fusion-project':
                discord_log.info('Joining Default Text Channel')
                bot.loop.create_task(check_subreddit(channel.id))

@bot.event
async def on_message(message):
    # don't reply to itself
    if message.author == bot.user:
        return
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)

# @bot.command()
# async def add(ctx, a: int, b: int):
#     await ctx.send(a+b)

# @bot.command()
# async def multiply(ctx, a: int, b: int):
#     await ctx.send(a*b)

# @bot.command()
# async def greet(ctx):
#     await ctx.send(":smiley: :wave: Hello, there!")

# @bot.command()
# async def cat(ctx):
#     await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

# @bot.command()
# async def info(ctx):
#     embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)
    
#     # give info about you here
#     embed.add_field(name="Author", value="<YOUR-USERNAME>")
    
#     # Shows the number of servers the bot is member of.
#     embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

#     # give users a link to invite thsi bot to their server
#     embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

#     await ctx.send(embed=embed)

# bot.remove_command('help')

# @bot.command()
# async def help(ctx):
#     embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)

#     embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
#     embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
#     embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
#     embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
#     embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
#     embed.add_field(name="$help", value="Gives this message", inline=False)

#     await ctx.send(embed=embed)


