import copy
import discord
from redbot.core import Config, commands, checks
from redbot.core.utils.chat_formatting import pagify

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]         
creds = ServiceAccountCredentials.from_json_keyfile_name("/home/pi/Bot_Archive/creds.json", scope)
client = gspread.authorize(creds)

class jp2021money(commands.Cog):
    """This bot reminds us about how much money we should have 
        saved up for the Japan trip planned for May 2021."""
    
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
    async def test(self, ctx):
        """test command"""
        # Call the Sheets API
        sheet = client.open("Bot Money Saving Goals").sheet1
        
        # initalize week list at 1
        week = 1
        
        # grab column containing sent data
        sent = sheet.col_values(2)
        
        # find the next row to send reminder
        while sent[week] != 'no':
            week+=1
            
        # cause the nested while/if loop didnt work... dont hurt me...
        if sent[week-1] == 'end':
            week-=1
            
        # check for end of list
        if sent[week] == 'end':
            # ping the role to be reminded
            # admin role
            role = '<@&232216294437421056>'
            await ctx.send(role)

            # constuct embedded message
            embed = discord.Embed(
                title = 'Japan 2021 Trip: Savings Reminder',
                description = """If I made this bot correctly, we shoud be currently at the end of April 2021 or the beginning of May 2021. \n\nAt this point, you should have reached the savings goal of at least **$2000**. If not, well uh, gambate...""",
                color = discord.Color.red()
            )
            footer = """Someone tell Erick to turn off this reminder. That dumbass. It\'s not like I wanted to remind you or anything, baka..."""
            embed.set_footer(text=footer)
            embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
            await ctx.send(embed=embed)
        
        else:
            saved = sheet.cell(week+1,3).value
            goal = sheet.cell(week+1,4).value

            # ping the role to be reminded
            # admin role
            role = '<@&232216294437421056>'
            # japan trip role
            #role = '<@&660958548024360960>'
            await ctx.send(role)

            # constuct embedded message
            embed = discord.Embed(
                title = 'Japan 2021 Trip: Savings Reminder',
                description = """Sup weebs, this is your weekly reminder on roughly how much money you should have saved for the trip. You should be saving at least **$30** each week to meet the goals set by this guideline.\n\nSo far, you should have roughly saved **%s/%s**.""" % (saved,goal),
                color = discord.Color.red()
            )
            footer = """These stretchgoals are not binding, but rather they serve as a guideline to keep our finances in check. It\'s not like I wanted to remind you or anything, baka..."""
            embed.set_footer(text=footer)
            embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
            await ctx.send(embed=embed)

            sheet.update_cell(week+1,2,"yes")
            sheet.update_cell(week+1,5,"yes")

