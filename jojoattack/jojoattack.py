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
        
        r = random.randint(0, 12)
        
        if r == 0:
        embed = discord.Embed(
            description = 'SANRAITO IERO OBADORAIBU!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://media2.giphy.com/media/SGGmDq71JY8uc/source.gif')
        await ctx.send(embed=embed)
        
        if r == 1:
        embed = discord.Embed(
            description = 'SANDA KUROSU SUPURITTO ATAKKU!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://media.giphy.com/media/Id6pn9N6DEgphsE1kF/giphy.gif')
        await ctx.send(embed=embed)
        
        if r == 2:
        embed = discord.Embed(
            description = 'KURAKKA VOREI!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://thumbs.gfycat.com/WelltodoSpicyCoral-size_restricted.gif')
        await ctx.send(embed=embed)
        
        if r == 3:
        embed = discord.Embed(
            description = 'NIGERUNDAYO!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://media.giphy.com/media/731iFlLiqaRk4/giphy.gif')
        await ctx.send(embed=embed)
        
        if r == 4:
        embed = discord.Embed(
            description = 'SHABON RANCHA!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://vignette.wikia.nocookie.net/powerlisting/images/f/f5/Caesar_Zeppeli%27s_Bubbles_%28JoJo%29.gif/revision/latest?cb=20190822152544')
        await ctx.send(embed=embed)
        
        if r == 5:
            embed = discord.Embed(
                description = 'ORA ORA ORA ORA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/4795d34aa49ada5299453dfa9960ee40/tenor.gif?itemid=5505650')
            await ctx.send(embed=embed)
        
        if r == 6:
        embed = discord.Embed(
            description = 'HAMITTO PAPURU!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://i.kym-cdn.com/photos/images/original/000/954/233/0e7.gif')
        await ctx.send(embed=embed)
        
        if r == 7:
            embed = discord.Embed(
                description = 'KUROSU FAIYA HARIKEN!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/777a6281d408665ff4d9e63488271d38/tenor.gif?itemid=14122005')
            await ctx.send(embed=embed)
        
        if r == 8:
            embed = discord.Embed(
                description = 'EMERARUDO SUPURASSHU!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/0de4104ef4493fd3ec12bc7d9c5ef36a/tenor.gif?itemid=14264200')
            await ctx.send(embed=embed)
        
        if r == 9:
        embed = discord.Embed(
            description = 'SHIRUBA CHARIOTTSU!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://pa1.narvii.com/6618/e37d28d7810ce7e0038db64cc64cc2137f0399b8_hq.gif')
        await ctx.send(embed=embed)
        
        if r == 10:
        embed = discord.Embed(
            description = 'ZA FURU!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://i.kym-cdn.com/photos/images/original/000/946/759/efd.gif')
        await ctx.send(embed=embed)
        
        if r == 11:
        embed = discord.Embed(
            description = 'ZA WARUDO!!!',
            color = discord.Color.red()
        )
        embed.set_image(url='https://media.giphy.com/media/nyNS6Cfrnkdj2/giphy.gif')
        await ctx.send(embed=embed)
        
        if r == 12:
            embed = discord.Embed(
                description = 'MUDA MUDA MUDA MUDA!!!',
                color = discord.Color.red()
            )
            embed.set_image(url='https://media1.tenor.com/images/b73575c3289f3d221fcb8089777b0549/tenor.gif?itemid=12851143')
            await ctx.send(embed=embed)
