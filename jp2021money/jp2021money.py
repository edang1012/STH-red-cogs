# google sheets API stuff
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# redbot stuff
import copy
import discord
from redbot.core import Config, commands, checks
from redbot.core.utils.chat_formatting import pagify

# google drive api from youtube
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# google sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '116sfWwMvsA6rsEE8qG6xrfAOlH1jG5jkGgQ24HWtEu0'
RANGE_NAME = 'A2:E'

# google drive API from youtube
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
    async def saving(self, ctx):
        """Japan 2021 Trip Savings Reminder"""
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
            #role = '<@&232216294437421056>'
            # japan trip role
            role = '<@&660958548024360960>'
            await ctx.send(role)

            # constuct embedded message
            embed = discord.Embed(
                title = 'Japan 2021 Trip: Savings Reminder (Week %s/Week 68)' % (week),
                description = """Sup weebs, this is your weekly reminder on roughly how much money you should have saved for the trip. You should be saving at least **$30** each week to meet the goals set by this guideline.\n\nSo far, you should have roughly saved **%s/%s**.""" % (saved,goal),
                color = discord.Color.red()
            )
            footer = """These stretchgoals are not binding, but rather they serve as a guideline to keep our finances in check. It\'s not like I wanted to remind you or anything, baka..."""
            embed.set_footer(text=footer)
            embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
            await ctx.send(embed=embed)

            sheet.update_cell(week+1,2,"yes")
            sheet.update_cell(week+1,5,"yes")

    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def testsheet(self, ctx):
        """Japan 2021 Trip Savings Reminder"""
        # Call the Sheets API
        sheet = client.open("Bot Money Saving Goals").sheet1
       
        # grab column data
        col = sheet.col_values(1)

        # test output message
        if col[0] == 'Week':
            msg = "I can talk to the sheet shishou!"
            await ctx.send(msg)





    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def beta(self, ctx):    
        """Shows basic usage of the Sheets API.
        Prints values from a sample spreadsheet.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,range=RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            msg = "Shishou, there is no data..."
            await ctx.send(msg)
            
        else:
            for row in values:
                if row[1] == 'yes':
                    print('yes')
                    
                else:
                    # ping the role to be reminded
                    # admin role
                    role = '<@&232216294437421056>'
                    # japan trip role
                    #role = '<@&660958548024360960>'
                    await ctx.send(role)

                    # constuct embedded message and send
                    embed = discord.Embed(
                        title = 'Japan 2021 Trip: Savings Reminder (Week %s/Week 68)' % (row[0]),
                        description = """Sup weebs, this is your weekly reminder on roughly how much money you should have saved for the trip. You should be saving at least **$30** each week to meet the goals set by this guideline.\n\nSo far, you should have roughly saved **%s/%s**.""" % (row[2],row[3]),
                        color = discord.Color.red()
                    )
                    footer = """These stretchgoals are not binding, but rather they serve as a guideline to keep our finances in check. It\'s not like I wanted to remind you or anything, baka..."""
                    embed.set_footer(text=footer)
                    embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
                    await ctx.send(embed=embed)
                    
                    cell = 'A3'
                    body = {
                        'values': 'yes'
                    }

                    cell_write = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID, range=cell, valueInputOption='RAW', body=body).execute()

                    break;

