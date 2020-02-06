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
    async def testo(self, ctx, arg):
        """Test a specific JoJo attack!"""
        
        msg = arg
        embed = self.jojo_embed(arg)
        
        await ctx.send(embed=embed)
    
    @commands.guild_only()
    @commands.command()
    async def jojo(self, ctx):
        """Use a random JoJo attack!"""
        
        rand = random.randint(0, 12)
        embed = self.jojo_embed(rand)
        
        await ctx.send(embed=embed)
    
    def jojo_embed(self, rand):
        """Make a JoJo attack embed!"""
        
        if rand == 0:
            embed = discord.Embed(
                description = 'SANRAITO IERO OBADORAIBU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media2.giphy.com/media/SGGmDq71JY8uc/source.gif')
            
            return embed
        
        if rand == 1:
            embed = discord.Embed(
                description = 'SANDA KUROSU SUPURITTO ATAKKU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media.giphy.com/media/Id6pn9N6DEgphsE1kF/giphy.gif')
            
            return embed
        
        if rand == 2:
            embed = discord.Embed(
                description = 'KURAKKA VOREI!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://thumbs.gfycat.com/WelltodoSpicyCoral-size_restricted.gif')
            
            return embed
        
        if rand == 3:
            embed = discord.Embed(
                description = 'NIGERUNDAYO!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media.giphy.com/media/731iFlLiqaRk4/giphy.gif')
            
            return embed
        
        if rand == 4:
            embed = discord.Embed(
                description = 'SHABON RANCHA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://thumbs.gfycat.com/HardTightArcticfox-size_restricted.gif')
            
            return embed
        
        if rand == 5:
            embed = discord.Embed(
                description = 'ORA ORA ORA ORA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/4795d34aa49ada5299453dfa9960ee40/tenor.gif?itemid=5505650')
            
            return embed
        
        if rand == 6:
            embed = discord.Embed(
                description = 'HAMITTO PAPURU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.kym-cdn.com/photos/images/original/000/954/233/0e7.gif')
            
            return embed
        
        if rand == 7:
            embed = discord.Embed(
                description = 'KUROSU FAIYA HARIKEN!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/777a6281d408665ff4d9e63488271d38/tenor.gif?itemid=14122005')
            
            return embed
        
        if rand == 8:
            embed = discord.Embed(
                description = 'EMERARUDO SUPURASSHU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/0de4104ef4493fd3ec12bc7d9c5ef36a/tenor.gif?itemid=14264200')
            
            return embed
        
        if rand == 9:
            embed = discord.Embed(
                description = 'SHIRUBA CHARIOTTSU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://pa1.narvii.com/6618/e37d28d7810ce7e0038db64cc64cc2137f0399b8_hq.gif')
            
            return embed
        
        if rand == 10:
            embed = discord.Embed(
                description = 'ZA FURU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://i.kym-cdn.com/photos/images/original/000/946/759/efd.gif')
            
            return embed
        
        if rand == 11:
            embed = discord.Embed(
                description = 'ZA WARUDO!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media.giphy.com/media/nyNS6Cfrnkdj2/giphy.gif')
            
            return embed
        
        if rand == 12:
            embed = discord.Embed(
                description = 'MUDA MUDA MUDA MUDA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/b73575c3289f3d221fcb8089777b0549/tenor.gif?itemid=12851143')
            
            return embed
