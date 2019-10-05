import copy
import discord
from redbot.core import Config, commands, checks
from redbot.core.utils.chat_formatting import pagify

class seqreact(commands.Cog):

    default_guild_settings = {
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
    async def addseq(self, ctx, word, emoji):
        """Add a sequence of reactions to a keyword/phrase
        Usage:  pass a keyword or keyphrase(in quotations) to <word>
                pass an emoji or emojis (in quotations) to <emoji>"""
        
        guild = ctx.message.guild
        message = ctx.message
        await self.create_reaction_sequence(guild, message, word, emoji)
        
        
    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def remseq(self, ctx, word, emoji):
        """Remove a sequence of reactions to a keyword/phrase
        Usage:  pass a keyword or keyphrase(in quotations) to <word>
                pass an emoji or emojis (in quotations) to <emoji>"""
        
        guild = ctx.message.guild
        message = ctx.message
        await self.remove_reaction_sequence(guild, word, emoji, message)
      
    
    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def listseq(self, ctx):
        """List reactions for this server"""
        emojis = await self.conf.guild(ctx.guild).reactions()
        msg = f"Smart Reactions for {ctx.guild.name}:\n"
        for emoji in emojis:
            for command in emojis[emoji]:
                msg += f"{emoji}: {command}\n"
        for page in pagify(msg, delims=["\n"]):
            await ctx.send(msg)
        
        
    async def create_reaction_sequence(self, guild, message, word, emoji):
        try:
            reactions = await self.conf.guild(guild).reactions()
            
            if emoji in reactions:
                if word.lower() in reactions[emoji]:
                    await message.channel.send("This reaction sequence already exists.")
                    return
                reactions[emoji].append(word.lower())
            else:
                reactions[emoji] = [word.lower()]
            await self.conf.guild(guild).reactions.set(reactions)
            await message.channel.send("Successfully added this reaction sequence.")

        except (discord.errors.HTTPException, discord.errors.InvalidArgument):
            await message.channel.send("Uh oh, something bad happened...")
            
            
    async def remove_reaction_sequence(self, guild, word, emoji, message):
        try:
            reactions = await self.conf.guild(guild).reactions()
            
            if emoji in reactions:
                if word.lower() in reactions[emoji]:
                    reactions[emoji].remove(word.lower())
                    await self.conf.guild(guild).reactions.set(reactions)
                    await message.channel.send("Removed this reaction sequence.")
                else:
                    await message.channel.send("That sequence is not for that word/phrase")
            else:
                await message.channel.send("There is no sequence to delete.")

        except (discord.errors.HTTPException, discord.errors.InvalidArgument):
            await message.channel.send("Uh oh, something bad happened...")
            
            
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.guild:
            return
        if message.author == self.bot.user:
            return
        guild = message.guild
        reacts = copy.deepcopy(await self.conf.guild(guild).reactions())
        if reacts is None:
            return
        words = message.content.lower().split()
        for emoji in reacts:
            #if set(w.lower() for w in reacts[emoji]).intersection(words):
            if reacts[emoji] in words:
                try:
                    #split emoji list into a list
                    emotes = emoji.split()

                    for i in emotes:
                        await message.add_reaction(i)
                        
                except discord.errors.Forbidden:
                    pass
                except discord.errors.InvalidArgument:
                    pass
