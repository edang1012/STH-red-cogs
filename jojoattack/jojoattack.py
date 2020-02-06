import discord
import os
import re
import random

from redbot.core import checks, Config, commands

BaseCog = getattr(commands, "Cog", object)


class jojoattack(BaseCog):

    """All STH reaction commands conveniently located in one file!"""

    default_global_settings = {
        "channels_ignored": [],
        "guilds_ignored": []
    }

    def __init__(self, bot):
        self.bot = bot
        self.conf = Config.get_conf(self, identifier=527690525)
        self.conf.register_global(
            **self.default_global_settings
        )

    @commands.guild_only()
    @commands.command()
    async def jojo(self, ctx):
        """Use a randomized JoJo attack!"""
        
        r = random.randint(0, 1)
        
        if r == 0:
            embed = discord.Embed(
                description = 'ORA ORA ORA ORA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://www.google.com/url?sa=i&url=https%3A%2F%2Ftenor.com%2Fsearch%2Fora-ora-ora-gifs&psig=AOvVaw3KISyXyEUb4EzCJjROAkgr&ust=1581084141702000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPCYi8eLvecCFQAAAAAdAAAAABAD')
            await ctx.send(embed=embed)
         
        if r == 1:
            embed = discord.Embed(
                description = 'MUDA MUDA MUDA MUDA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://www.google.com/url?sa=i&url=https%3A%2F%2Ftenor.com%2Fview%2Fmuda-the-world-punch-jo-jos-bizarre-adventure-gif-12851143&psig=AOvVaw3NDGv85B6GMymokmyGn1xg&ust=1581084259673000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCID3rv-LvecCFQAAAAAdAAAAABAD')
            await ctx.send(embed=embed)
