import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from models import *

load_dotenv()
TOKEN = os.getenv('DISCORD_API_TOKEN') # bot token for the discord api
bot = commands.Bot(command_prefix='!')

games = dict() # TODO: there's probably a better way to do this

@bot.event # show yourself!
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

# simple testing command
@bot.command() 
async def ping(ctx):
    await ctx.send('pong!')
    
    
# slightly more complicated testing command
@bot.command() 
async def identity(ctx, *args):
    await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

@bot.command(name='new', aliases=['n'])
async def name(ctx, data, object):
    if (data == "game"):
        if (not (object in games)):
            games[object] = Game.create(object)
            await ctx.send('Creating a game named "{}"'.format(object))
            await ctx.send('Would you like to use a ruleset template?')
            # TODO get a response from the user somehow...
        else:
            await ctx.send('That game name is already in use.')
    # TODO: cases for "character" and "scene"
            

bot.run(TOKEN)
