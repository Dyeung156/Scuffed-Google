# bot.py
import os

import discord, random, asyncio
from dotenv import load_dotenv
from discord import Member
from itertools import cycle

load_dotenv()
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!', description='SBU HACKS BOT!!')
TOKEN = os.environ.get('TOKEN', 3)


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