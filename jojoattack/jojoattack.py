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
    async def jojoattack(self, ctx):
        """Use a randomized JoJo attack!"""
        
        r = random.randint(0, 10)

        embed = discord.Embed(
            description = 'ITS TIME MOTHERFUCKER!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://media1.tenor.com/images/316802abc29c277b08bae799b1fbe52c/tenor.gif')
        await ctx.send(embed=embed)
