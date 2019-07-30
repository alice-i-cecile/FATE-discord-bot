import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from models import *
import utils
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_API_TOKEN') # bot token for the discord api
TIMEOUT = 10 # global timeout for bot prompts
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

# group for creating new objects
@bot.group(name='new', aliases=['n'])
async def new(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Please specify a type.')
        
# new game instance
@new.command()
async def game(ctx, object: str): # TODO proper error handling if object is not given (i think there's a nice way to do this)
    if (not (object in games)): #make a new game babey!
        await ctx.send('Creating a game named "{}"'.format(object))
        await ctx.send('Would you like to use a ruleset template?')
        try: # block to catch message timeouts
            res = await bot.wait_for('message', check=utils.same_author_channel(ctx), timeout=TIMEOUT)
            games[object] = Game.create(object)
        except asyncio.TimeoutError:
            await ctx.send('Prompt timed out.')
    else:
        await ctx.send('That game name is already in use.')
            
bot.run(TOKEN)
