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

# create discord bot and pass it credentials as well as other connections
cred = credentials.read_credentials('discord')
bot = commands.Bot(command_prefix=("`"))
bot.subreddit = sr
bot.backend = db


def start_discord_bot():
    # bot.loop.create_task(check_subreddit())
    bot.run(cred['discord']['bot_token'])



async def check_subreddit(channel_id):
    await bot.wait_until_ready()
    channel = bot.get_channel(channel_id)
    while not bot.is_closed():
        await channel.send('Hold on while I check reddit...')
        discord_log.info('Checking subreddit for new posts.')
        bot.subreddit.check_for_new_posts()
        await asyncio.sleep(30)

@bot.event
async def on_ready():
    discord_log.info('Logged in as')
    discord_log.info(bot.user.name)
    discord_log.info(bot.user.id)
    discord_log.info('Using discord.py version: {}'.format(discord.__version__))
    discord_log.info('------')
    # LINK TO SUBREDDIT
    for guild in bot.guilds:
        # discord_log.info("Server: {}".format(server.name))
        for channel in guild.channels:
            # discord_log.info("  {} {} {}".format(channel.name, channel.type, channel.id))
            if isinstance(channel, discord.TextChannel) and channel.name == 'fusion-project':
                discord_log.info('Joining Default Text Channel')
                bot.loop.create_task(check_subreddit(channel.id))

@bot.event
async def on_message(message):
    # don't reply to itself
    if message.author == bot.user:
        return
    if message.content[1:].startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    # move on to process any commands
    await bot.process_commands(message)

# @bot.command()
# async def multiply(ctx, a: int, b: int):
#     await ctx.send(a*b)

# @bot.command()
# async def greet(ctx):
#     await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def status(ctx):
    embed = discord.Embed(title="System Status", description="dungeon_bot services")
    if bot.subreddit.check_for_new_posts():
        embed.add_field(name="Subreddit", value="Good")#, color=0x57ee72)
    else:
        embed.add_field(name="Subreddit", value="Bad")#, color=0xee5768)
    if bot.backend.check_db():
        embed.add_field(name="Database", value="Good")#, color=0x57ee72)
    else:
        embed.add_field(name="Database", value="Bad")#, color=0xee5768)
    # check for DM online?
    await ctx.send(embed=embed)

@bot.command()
async def dbcheck(ctx):
    await ctx.send(str(bot.backend.get_tables()))

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="dungeon_bot", description="A D&D DM helper bot, id est a minion.", color=0xeee657)
    # give info about you here
    embed.add_field(name="Author", value="chisaipete")    
    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    # # give users a link to invite thsi bot to their server
    # embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")
    await ctx.send(embed=embed)

bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed = discord.Embed(title="dungeon_bot", description="A D&D DM helper bot, id est a minion. List of commands are:", color=0xeee657)

    # embed.add_field(name="`multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    # embed.add_field(name="`greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="`dbcheck", value="Gives result of database check.", inline=False)
    embed.add_field(name="`status", value="Gives current status of services.", inline=False)


    embed.add_field(name="`info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="`help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)


