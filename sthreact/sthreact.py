import os
import re

from redbot.core import checks, Config, commands

BaseCog = getattr(commands, "Cog", object)


class sthreact(BaseCog):

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

    @commands.group(name="sthreact_ignore", pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_guild=True)
    async def sthreact_ignore(self, ctx):
        """Change Oh my cog ignore settings."""
        pass

    @sthreact_ignore.command(name="server", pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_guild=True)
    async def _sthreact_ignore_server(self, ctx):
        """Ignore/Unignore the current server"""

        guild = ctx.message.guild
        guilds = await self.conf.guilds_ignored()
        if guild.id in guilds:
            guilds.remove(guild.id)
            await ctx.send("wot? Ok boss, I will no longer "
                           "ignore this server.")
        else:
            guilds.append(guild.id)
            await ctx.send("what? Fine, I will ignore "
                           "this server.")
        await self.conf.guilds_ignored.set(guilds)

    @sthreact_ignore.command(name="channel", pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_guild=True)
    async def _sthreact_ignore_channel(self, ctx):
        """Ignore/Unignore the current channel"""

        chan = ctx.message.channel
        chans = await self.conf.channels_ignored()
        if chan.id in chans:
            chans.remove(chan.id)
            await ctx.send("nani? Ok, I will no longer "
                           "ignore this channel.")
        else:
            chans.append(chan.id)
            await ctx.send("nani? Alright, I will ignore "
                           "this channel.")
        await self.conf.channels_ignored.set(chans)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.guild is None:
            return
        if message.author == self.bot.user:
            return
        #content = message.content.lower().split()
        content = message.content.lower()
        if len(content) < 2:
            return
        if message.guild.id in await self.conf.guilds_ignored():
            return
        if message.channel.id in await self.conf.channels_ignored():
            return

        
        #pattern1 = re.match(r"oh", content[0])
        #pattern2 = re.match(r"my", content[1])
        pattern0 = "test phrase"
        pattern1 = "oh my"
        
        if pattern0 in content:
            msg = "it works!!! shishou"
            await message.channel.send(msg)
            
        elif pattern1 in content:
            msg = "https://i.makeagif.com/media/2-21-2015/RDVwim.gif \noh my...\nomae...\nOMAE WA MOU SHINDEIRU!!!"
            await message.channel.send(msg)
