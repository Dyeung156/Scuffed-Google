# bot.py
import os

import discord, random, asyncio
from dotenv import load_dotenv
from discord import Member
from itertools import cycle

load_dotenv()
from discord.ext import commands, tasks


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_exec_shim = os.environ.get("GOOGLE_CHROME_BIN", "chromedriver")
opts = webdriver.ChromeOptions()
opts.binary_location = chrome_exec_shim
opts.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install())


bot = commands.Bot(command_prefix='?', description='SBU HACKS BOT!!')
TOKEN = os.environ.get('TOKEN', 3)

@bot.event
async def on_ready():
    party = bot.get_emoji(698725283649290310)
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="your data ;)", emoji=party))
    print('bot.py is active')





@bot.command(name='hello')
async def hello(ctx):
    await ctx.send("hey sup lol")

@bot.command(name="join")
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name="leave")
async def join(ctx):
    await ctx.voice_client.disconnect()

@bot.command(name="google")
async def join(ctx, *, search):
    driver.get("https://google.com")

# ---------------------------------------

@bot.command(hidden=True)
async def load(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command(hidden=True)
async def unload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'cogs.{filename[:-3]}')


@bot.command(hidden=True)
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.unload_extension(f'cogs.{filename[:-3]}')
            bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)