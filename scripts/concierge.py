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
        await ctx.send('Invalid onboarding [ob] command passed...')

@ob.command()
async def add_player(ctx, arg):
    await ctx.send('You want to add {} as a new player?'.format(arg))
    # what's their email address
    # what's their phone number

@ob.command()
async def make_dm(ctx, arg):
    await ctx.send('You are now a DM! Use your power wisely.')
    # what's the password? https://github.com/pyotp/pyotp
    # this is a toggle command, executing once, makes the player a DM, executing again, removes DM-ship

@ob.command()
async def reddit(ctx, arg):
    # check if a player profile exists for the messenger, unless the messenger is a DM
    await ctx.send('You want to add {} to your Player profile?'.format(arg))

@ob.command()
async def discord(ctx, arg):
    # check if a player profile exists for the messenger, unless the messenger is a DM
    await ctx.send('You want to add {} to your Player profile?'.format(arg))
# End Onboarding Commands

# Player Stats Commands
@bot.group()
async def stats(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid statistics [stats] command passed...')

@stats.command(aliases=['money', '$', 'wealth', 'g'])
async def gold(ctx, arg):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['exp', 'xp', 'x'])
async def experience(ctx, arg):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['lvl', 'l'])
async def level(ctx, arg):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['room', 'rooms', 'hotel', 'motel', 'r'])
async def inn(ctx, arg):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['horse', 'car', 'transport', 's'])
async def stable(ctx, arg):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['bank', 'box', 'chest', 'b'])
async def safe(ctx, arg):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['inv', 'i'])
async def inventory(ctx, arg):
    await ctx.send('{}'.format(arg))

@stats.command(aliases=['tok', 'token', 't'])
async def tokens(ctx, arg):
    await ctx.send('{}'.format(arg))

# End Player Stats Commands
