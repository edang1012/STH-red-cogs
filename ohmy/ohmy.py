import os
import re

from redbot.core import checks, Config, commands

BaseCog = getattr(commands, "Cog", object)


class Ohmy(BaseCog):

    """Tu ya estas muertos!!!"""

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

    @commands.group(name="ohmyignore", pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_guild=True)
    async def ohmyignore(self, ctx):
        """Change Oh my cog ignore settings."""
        pass

    @ohmyignore.command(name="server", pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_guild=True)
    async def _ohmyignore_server(self, ctx):
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

    @ohmyignore.command(name="channel", pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_guild=True)
    async def _ohmyignore_channel(self, ctx):
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

    # Come up with a new method to ignore bot commands
    async def on_message(self, message):
        if message.guild is None:
            return
        if message.author.bot:
            return
        #if self.is_command(message):
        #    return
        content = message.content.lower().split()
        if len(content) != 1:
            return
        if message.guild.id in await self.conf.guilds_ignored():
            return
        if message.channel.id in await self.conf.channels_ignored():
            return

        pattern = re.compile(r'o+h+m+y+[.?!]*', re.IGNORECASE)
        if pattern.fullmatch(content[0]):
            async for before in message.channel.history(limit=5, before=message):
                msg = "https://i.makeagif.com/media/2-21-2015/RDVwim.gif \n oh my...\nomae...\nOMAE WA MOU SHINDEIRU!!!"
                await message.channel.send(msg)
