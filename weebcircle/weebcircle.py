
import discord
import os
import re

from redbot.core import checks, Config, commands


class weebcircle(commands.Cog):
    """This bot was made to be used for weebcircle things."""
    
    default_guild_settings = {
        "settings": {}
    }

    def __init__(self, bot):
        self.bot = bot
        self.conf = Config.get_conf(self, identifier=964952632)
        self.conf.register_guild(
            **self.default_guild_settings
            )
        

    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def ping(self, ctx, member: discord.member):
        await ctx.send(f"PONG {member}")
