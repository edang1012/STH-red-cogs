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
        
        r = random.randint(0, 2)
        
        if r == 0:
            embed = discord.Embed(
                description = 'ORA ORA ORA ORA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/4795d34aa49ada5299453dfa9960ee40/tenor.gif?itemid=5505650')
            await ctx.send(embed=embed)
         
        if r == 1:
            embed = discord.Embed(
                description = 'MUDA MUDA MUDA MUDA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/b73575c3289f3d221fcb8089777b0549/tenor.gif?itemid=12851143')
            await ctx.send(embed=embed)
        
        if r == 2:
            embed = discord.Embed(
                description = 'EMERARUDO SUPURASSHU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/0de4104ef4493fd3ec12bc7d9c5ef36a/tenor.gif?itemid=14264200')
            await ctx.send(embed=embed)
