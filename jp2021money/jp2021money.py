import copy
import discord
from redbot.core import Config, commands, checks
from redbot.core.utils.chat_formatting import pagify

class jp2021money(commands.Cog):

    default_guild_settings = {
        #remove this when i figure out what this does
        "reactions": {}
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
    async def listseq(self, ctx):
        """test command"""
        msg = "test command stuff"
        await ctx.send(msg)
  
