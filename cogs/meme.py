# meme.py
import discord, random, asyncio
from discord.ext import commands
from discord import Member

import colorama
from colorama import Fore
from colorama import Style

def attachm(message):
    if (len(message.attachments) > 0 or 'https://' in message.content):
        return True
    else:
        return False

class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(Fore.WHITE + Style.BRIGHT + 'meme.py is active' + Style.RESET_ALL)
        
    @commands.command()
    async def meme(self,ctx):
        channelid = 891378663323500625
        channel = self.bot.get_channel(channelid)
        async for messageM in channel.history(limit=20):
            if (9 == random.randint(0,10)):
                await ctx.channel.send(messageM.content)
                return


    @commands.Cog.listener()
    async def on_message(self, message):
        if attachm(message) and not (self.bot.get_emoji(776161705960931399) in message.reactions):
            await message.add_reaction('<:upvote:776161705960931399>')
            await message.add_reaction('<:downvote:776162465842200617>')

                                
    @commands.Cog.listener()
    async def on_message_edit(self, old, message):
        if attachm(message) and not (self.bot.get_emoji(776161705960931399) in message.reactions):
            await message.add_reaction('<:upvote:776161705960931399>')
            await message.add_reaction('<:downvote:776162465842200617>')


def setup(bot):
    bot.add_cog(meme(bot))
