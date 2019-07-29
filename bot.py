import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_API_TOKEN') # bot token for the discord api
bot = commands.Bot(command_prefix='!')

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



bot.run(TOKEN)
