import copy
import discord
from redbot.core import Config, commands, checks
from redbot.core.utils.chat_formatting import pagify

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/sprea...,"https://www.googleapis.com/auth/drive...","https://www.googleapis.com/auth/drive"]
         
class jp2021money(commands.Cog):
    """This bot reminds us about how much money we should have 
        saved up for the Japan trip planned for May 2021."""
    
    default_guild_settings = {
        "money": {}
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
    async def test(self, ctx):
        """test command"""
        # Call the Sheets API
   
        embed = discord.Embed(
            title = 'Title',
            description = 'This is a description',
            color = discord.Color.red()
        )
        embed.set_footer(text='This is a footer')
        embed.set_image(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
        embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
        embed.add_field(name='Field Name', value='Field Value', inline=False)
        await ctx.send(embed=embed)
