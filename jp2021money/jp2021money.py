from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import copy
import discord
from redbot.core import Config, commands, checks
from redbot.core.utils.chat_formatting import pagify

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1SOskKBFHYbVvdGIJ0ExGXCGYmSlajqUJDHHbVOlzGug'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'


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
        self.creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    '/home/pi/redbot-beta/cogs/CogManager/cogs/jp2021money/credentials.json', SCOPES)
                self.creds = flow.run_local_server()
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('sheets', 'v4', credentials=self.creds)
        

    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def test(self, ctx):
        """test command"""
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
   
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

        if not values:
            msg = "No data found"
            await ctx.send(msg)

        else:
            print('Test:')
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print ('%s' % (row[0]))
                
                
    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def test2(self, ctx):
        """test2 command"""
        # Call the Sheets API
        sheet = self.service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
   
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

        if not values:
            msg = "No data found"
            await ctx.send(msg)

        #else:
            #print('Name, Major:')
            #for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                #msg = ('%s, %s' % (row[0], row[4]))
                

