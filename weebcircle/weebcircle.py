import discord
import os
import re
import pickle
import random
import numpy as np

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
        #self.rand = []
        self.old =  []

        
    @commands.guild_only()
    @commands.command()
    async def start(self, ctx):
        
        # create embed welcome message, no real code here, just formatting
        embed = discord.Embed(
            title = 'Welcome to the Weeb Circle',
            description = """The purpose of this circle is to get others in the group to watch anime they haven't seen before.""",
            color = discord.Color.red()
        )
        footer = """Why are you looking down here baka..."""
        embed.set_footer(text=footer)
        embed.add_field(name='**Instructions:**', 
                        value=("To start the circle, please follow the procedure listed below:\n\n"

                        "1.  **\".optin <count>\"**:\nUse this command to opt into the circle. " 
                                                    "Specify the number of cours you want to watch with a number or keywords such as: *easy, med, hard*. " 
                                                    "\nIf you want to opt out after opting in, simply use the command **\".optout\"**.\n\n"

                        "2.  **\".randomize\"**:     \nUse this command to create a randomized list for the members to recommend "
                                                    "anime. This is a mod/admin only command.\n\n"

                        "3.  **\".rec <anime>\"**:   \nUse this command to recommend an anime to your assigned member. \nIf you want "
                                                    "to see who is your assigned member use the command **\".list\"**.\n\n"

                        "4.  **\".watch\"**:         \nUse this command to display the final list of what each member is watching. " 
                                                    "\n\n"), 
                        inline=False
        )
        embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
        await ctx.send(embed=embed)
        
        
    @commands.guild_only()
    @commands.command()
    async def optin(self, ctx, arg1):
        """Usage: Enter the number of cours you would like to watch\n
        Input any number of cours or specify with the keywords below:
        1 cour:   1, Easy, Wolf
        2 cours:  2, Med, Medium, Tiger
        3 cours:  3, Hard, Demon
        3+ cours: Expert, Dragon, Ryu"""
        
        # open list from file to ensure most up to date version
        with open('/home/pi/Bot_Archive/weeb_list.data', 'rb') as f:
            self.list = pickle.load(f)
        
        # check if author is in list already
        if any(ctx.author.mention in list for list in self.list):
            msg = "You are already in the list baka"
        
        # bunch of cases for the input
        else:
            if arg1.isnumeric():
                self.list.append([ctx.author.mention, arg1])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "{} has been added to the list and wants at most {} cour(s).".format(ctx.author.mention,arg1)
            
            elif (arg1.lower() == 'easy') or (arg1.lower() == 'wolf') or (arg1.lower() == 'okami'):
                self.list.append([ctx.author.mention, '1'])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "{} has been added to the list and wants at most 1 cour.".format(ctx.author.mention)
            
            elif (arg1.lower() == 'med') or (arg1.lower() == 'medium') or (arg1.lower() == 'tiger') or (arg1.lower() == 'tora'):
                self.list.append([ctx.author.mention, '2'])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "{} has been added to the list and wants at most 2 cours.".format(ctx.author.mention)
                
            elif (arg1.lower() == 'hard') or (arg1.lower() == 'demon') or (arg1.lower() == 'oni'):
                self.list.append([ctx.author.mention, '3+'])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "{} has been added to the list and wants at most 3 cours.".format(ctx.author.mention)
            
            elif (arg1.lower() == 'expert') or (arg1.lower() == 'dragon') or (arg1.lower() == 'ryu'):
                self.list.append([ctx.author.mention, '3+'])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "{} has been added to the list and wants 3+ cours.".format(ctx.author.mention)
            
            elif (arg1.lower() == 'god') or (arg1.lower() == 'kami'):
                self.list.append([ctx.author.mention, '3+'])
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                msg = "Just pick something from here: https://en.wikipedia.org/wiki/List_of_anime_series_by_episode_count \nEnjoy ya damn masochist..."
            
            else:
                msg = "Thats not a valid number of cours, baka..."
                
        await ctx.send(msg)
        
        
    @commands.guild_only()
    @commands.command()
    async def optout(self, ctx):
        # open list from file to ensure most up to date version
        with open('/home/pi/Bot_Archive/weeb_list.data', 'rb') as f:
            self.list = pickle.load(f)
        
        # go through list to find author and remove
        for member in self.list:
            if ctx.author.mention == member[0]:
                self.list.remove(member)
        
        # update the list
        with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
            pickle.dump(self.list,f)
            
        msg = "{} has been removed from the list.".format(ctx.author.mention)
        await ctx.send(msg)
                
        
    @commands.guild_only()
    @commands.command()
    async def rec(self, ctx, *, arg):
        """Usage: Recommend an anime using this command"""
        
        # check if author is in list
        if not any(ctx.author.mention in list for list in self.list):
            msg = "You can't recommend unless you are in the list, baka..."
        
        # look for author in list
        #for member,rand in zip(self.list,self.rand):
        for member in self.list:
            if member[0] == ctx.author.mention:
                
                # check if author has already recommended
                # could break cause hard coding index, but will add length checks
                # to ensure commands can only work in a certain order
                if len(member) >= 3:
                    member[2] = arg
                    
                else:
                    member.extend([arg])
                              
                with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
                    pickle.dump(self.list,f)
                              
                msg = "{} recommended {} to {}".format(ctx.author.mention, arg, member[2])
                
        await ctx.send(msg)
        
        
    @commands.guild_only()
    @commands.command()
    async def oldlist(self, ctx):
        # debug command to check if the oldlist was saved, nothing important
        msg = "This is the oldlist:\n"

        for member in self.old:
            msg += "member[0]{}     member[1]{}     member[0][0]{}\n".format(member[0],member[1],member[0][0])
        await ctx.send(msg)
        
        
    @commands.guild_only()
    @commands.command()
    async def list(self, ctx):
        # debug command to ensure list is properly populated
        # open list from file to ensure most up to date version
        with open('/home/pi/Bot_Archive/weeb_list.data', 'rb') as f:
            self.list = pickle.load(f)
            
        msg = "Current members:\n"

        for member in self.list:
            msg += "{}\n".format(member)

        await ctx.send(msg)
        
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    @commands.command()
    async def clear(self, ctx):
        # debug command, to clear the list
        
        # set list to empty list
        self.list = []
        
        # write empty list to file
        with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
            pickle.dump(self.list,f)
            
        msg = "The list has been cleared"
        await ctx.send(msg)
        
        
    @commands.guild_only()
    @checks.admin_or_permissions(manage_guild=True)
    @commands.command()
    async def randomize(self, ctx):
        # open list from file to ensure most up to date version
        with open('/home/pi/Bot_Archive/weeb_list.data', 'rb') as f:
            self.list = pickle.load(f)
        
        # create numpy arrays for random function
        rand_array = np.array(self.list)
        old_array = np.array(self.list)
        
        # keep randomizing list until no one recommends themself
        # TODO: add a check to the oldlist so people dont get matched
        # two lists in a row
        while (rand_array[:,0] == old_array[:,0]).any():
            np.random.shuffle(rand_array)
        
        # convert numpy array back to lists since its just easier
        #self.rand = rand_list.tolist()
        rand_list = rand_array.tolist()
        self.list = old_array.tolist()
        
        # figure out why this doesnt work
        for member,rand in zip(self.list,rand_list):
            member.extend([rand[0]])
        
        with open('/home/pi/Bot_Archive/weeb_list.data', 'wb') as f:
            pickle.dump(self.list,f)
        
        msg = "Not Rand:\n"
        for member in self.list:
            msg += "{} wants to watch ".format(member[0])
            msg += "{} cour(s)\n".format(member[1])
            
        msg += "\n\n Rand:\n"
        for member in rand_list:
            msg += "{} wants to watch ".format(member[0])
            msg += "{} cour(s)\n".format(member[1])
        
        await ctx.send(msg)

    @commands.guild_only()
    @commands.command()
    async def watch(self, ctx):
        msg = "none"
        
        for member in self.list:
            if len(member) < 3:
                msg = "{} needs to recommend something.".format(member[0])
                
        if msg == "none":
            msg = "everyone rec'd something"
            
            self.old = self.list
                
            

        await ctx.send(msg)
