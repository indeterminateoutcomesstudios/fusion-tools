#? command to see your current stats (exp, gold, level, rooms, items)
#general operations
#get link to latest table map
#get link to latest write-ups player was involved with
#allow players to name their accountant :)
#Party formation (scheduling submission) - reddit
# Character wealth tracking
# Character advancement tracking (xp awarded per session, current level)
# 
import discord
from discord.ext import commands
from discordbot import bot

# Onboarding Commands
@bot.group()
async def ob(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('No onboarding subcommand passed: [ob <subcommand>]')

@ob.command()
async def add_player(ctx, name=None, email=None, phone=None):
    if name and email and phone:
        if ' ' in name and '@' in email:
            bot.backend.add_player(name, email, int(phone))
            await ctx.send('Player added!')
        else:
            await ctx.send('Error while adding player, check arguments.')
    else:
        await ctx.send('Try again: [ ob add_player "John Doe" jd@gmail.com 5091235555 ]')

@ob.command()
async def make_admin(ctx, player=None):
    #TODO: resolve to full discord name
    if not player:
        player = ctx.message.author

    if bot.backend.check_admin(bot.backend.get_player_id(discord=player))    

    await ctx.send('{} is now an administrator! Use your power wisely.'.format(player))
    # what's the password? https://github.com/pyotp/pyotp
    # this is a toggle command, executing once, makes the player a DM, executing again, removes DM-ship

@ob.command()
async def add_reddit(ctx, player=None, account=None):
    await ctx.send('You want to add {} to your Player profile?'.format(account))

@ob.command()
async def add_discord(ctx, player=None, account=None):
    #TODO: resolve to full discord name
    if not player:
        player = ctx.message.author
    await ctx.send('You want to add {} to your Player profile?'.format(player))
# End Onboarding Commands

# Player Stats Commands
@bot.group()
async def stats(ctx):
    if ctx.invoked_subcommand is None:
        # await ctx.invoke(bot.get_command('help stats'))
        # await ctx.send('Invalid statistics [stats] command passed...')
        pass
 
@stats.command(aliases=['money', '$', 'wealth', 'g'])
async def gold(ctx, arg=None):
    if isinstance(arg, int):
        #lookup pc # in database
        answer = 'foo'
    elif isinstance(arg, str):
        #lookup pc name in database
        answer = 'bar'
    else:
        answer = "Please specify your Character: [ ID# | Name ]"
    await ctx.send('{}'.format(answer))

@stats.command(aliases=['exp', 'xp', 'x'])
async def experience(ctx, arg=None):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['lvl', 'l'])
async def level(ctx, arg=None):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['room', 'rooms', 'hotel', 'motel', 'r'])
async def inn(ctx, arg=None):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['horse', 'car', 'transport', 's'])
async def stable(ctx, arg=None):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['bank', 'box', 'chest', 'b'])
async def safe(ctx, arg=None):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['inv', 'i'])
async def inventory(ctx, arg=None):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['tok', 'token', 't'])
async def tokens(ctx, arg=None):
    await ctx.send('{}'.format(arg))

# End Player Stats Commands
