import discord
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

        
        pattern0 = re.compile(r'(test)+( phrase)?', re.IGNORECASE)
        pattern1 = re.compile(r'(sigh)+[.]*', re.IGNORECASE)
        pattern2 = re.compile(r'(oh my)', re.IGNORECASE)
        
        if re.search(pattern0, content):
            msg = "it works!!! shishou"
            await message.channel.send(msg)
            
            content_split = content.split()
            if "embed" in content_split[1]:
                embed = discord.Embed(
                    title = 'Title',
                    description = 'This is a description',
                    colour = discord.Colour.blue()
                )
                embed.set_footer(text='This is a footer')
                embed.set_image(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
                embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/1148502291692965889/rdZ5NNWh_400x400.png')
                embed.add_field(name='Field Name', value='Field Value', inline=False)
                await message.channel.send(embed=embed)

        if re.search(pattern1, content):
            embed = discord.Embed(
                    colour = discord.Colour.red()
                )
            embed.set_image(url='https://media1.tenor.com/images/316802abc29c277b08bae799b1fbe52c/tenor.gif')
            embed.add_field(name='oh my', value='sign...', inline=False)
            await message.channel.send(embed=embed)
            
            #msg = "https://media1.tenor.com/images/316802abc29c277b08bae799b1fbe52c/tenor.gif \n\nsigh...\nsai...\nSAIDO CHESTO!!"
            #await message.channel.send(msg)
            
        if re.search(pattern2, content):
            msg = "https://i.makeagif.com/media/2-21-2015/RDVwim.gif \n\noh my...\nomae...\nOMAE WA MOU SHINDEIRU!!!"
            await message.channel.send(msg)
