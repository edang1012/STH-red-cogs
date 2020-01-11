import discord
import os
import re
import pickle

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
        self.list = []
        

    @commands.guild_only()
    @commands.command()
    async def weebping(self, ctx):
        msg = "<:ayaya:611753251888562187> {}".format(ctx.author.mention)
        await ctx.send(msg)

        
    @commands.guild_only()
    @commands.command()
    async def optin(self, ctx, arg1):
        self.circle.append([ctx.author.mention, arg1])
        with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
            pickle.dump(self.circle,f)
        msg = "{} has been added to the circle and wants {} cour.".format(ctx.author.mention,arg1)
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
    async def rec(self, ctx, *, arg):
        msg = "You said {}".format(arg)
        await ctx.send(msg)
        
    @commands.guild_only()
    @commands.command()
    async def list(self, ctx):
        with open('/home/pi/Bot_Archive/weeb_list.data', 'rb') as f:
            self.list = pickle.load(f)
            
        msg = "Currently members:\n"

        for member in self.list:
            msg += "{}\n".format(member)
        await ctx.send(msg)

    @commands.guild_only()
    @commands.command()
    async def print(self, ctx):
        
        msg = "Currently members:\n"
        for member in self.list:
            msg += "{} wants to watch ".format(member)
            for cour in member:
                msg += "{} cours\n".format(cour)
        await ctx.send(msg)
