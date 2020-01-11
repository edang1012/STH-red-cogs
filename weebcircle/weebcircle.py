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
        self.circle = []
        

    @commands.guild_only()
    @commands.command()
    async def weebping(self, ctx):
        msg = "<:ayaya:611753251888562187> {}".format(ctx.author.mention)
        await ctx.send(msg)

        
    @commands.guild_only()
    @commands.command()
    async def optin(self, ctx):
        self.circle.append(ctx.author.mention)
        msg = "{} has been added to the circle".format(ctx.author.mention)
        await ctx.send(msg)
        
        
    @commands.guild_only()
    @commands.command()
    async def circle(self, ctx):
        msg = "Currently members:\n"
        
        for member in self.circle:
            msg += "{}\n".format(member)
        
        await ctx.send(msg)
        
    @commands.guild_only()
    @commands.command()
    async def rec(self, ctx):
        msg = ctx.message
        await ctx.send(msg)
