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
        self.list = []
        

    @commands.guild_only()
    @commands.command()
    async def weebping(self, ctx):
        msg = "<:ayaya:611753251888562187> {}".format(ctx.author.mention)
        await ctx.send(msg)

        
    @commands.guild_only()
    @commands.command()
    async def optin(self, ctx, arg1):
        """Usage: Enter the number of cours you would like to watch
        1 cour: 1, Easy, Wolf
        2 cour: 2, Med, Medium, Tiger
        3 cour: 3, Hard, Demon"""
        
        if any(ctx.author.mention in list for list in self.list):
            msg = "You are already in the list baka"
            
        else:
            if arg1.isnumeric():
                self.list.append([ctx.author.mention, arg1])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "{} has been added to the list and wants {} cour.".format(ctx.author.mention,arg1)
            
            elif (arg1.lower() == 'easy') or (arg1.lower() == 'wolf'):
                self.list.append([ctx.author.mention, '1'])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "{} has been added to the list and wants 1 cour.".format(ctx.author.mention)
                
            else:
                msg = "Thats not a valid number of cours, baka..."
                
        await ctx.send(msg)
        
    @commands.guild_only()
    @commands.command()
    async def optout(self, ctx):
        for member in self.list:
            if ctx.author.mention == member[0]:
                self.list.remove(member)
                
        with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
            pickle.dump(self.list,f)
        msg = "{} has been removed from the list.".format(ctx.author.mention)
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
        with open('/home/pi/Bot_Archive/weeb_list.data', 'rb') as f:
            self.list = pickle.load(f)
        
        msg = "Currently members:\n"
        for member in self.list:
            msg += "{} wants to watch ".format(member[0])
            msg += "{} cour(s)\n".format(member[1])
        await ctx.send(msg)

    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    @commands.command()
    async def clear(self, ctx):
        self.list = []
        with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
            pickle.dump(self.list,f)
        msg = "The list has been cleared"
        await ctx.send(msg)
