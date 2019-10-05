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
    async def test(self, ctx, word, emoji):
        """Create a sequence of reactions to a keyword/phrase'
        Usage:  pass a keyword or keyphrase(in quotations) to <word>
                pass an emoji or emojis (in quotations) to <emoji>"""
        
        guild = ctx.message.guild
        message = ctx.message
        await self.create_reaction_sequence(guild, message, word, emoji)
        
    @checks.mod_or_permissions(administrator=True)
    @commands.guild_only()
    @commands.command()
    async def test1(self, ctx, word, emoji):
        """Delete an auto reaction to a word"""
        guild = ctx.message.guild
        message = ctx.message
        await self.remove_reaction_sequence(guild, word, emoji, message)
      
        
    async def create_reaction_sequence(self, guild, message, word, emoji):
        try:
            # Use the reaction to see if it's valid
            #await message.add_reaction(emoji)
            #test = emoji.split(" ")
            #for x in test:
            #    if ':' in x:
            #        await message.channel.send(x)
                            
            #emoji = str(emoji)
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
            emoji = str(emoji)
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
            if set(w.lower() for w in reacts[emoji]).intersection(words):
                try:
                    emotes = emoji.split(" ")
                    #check to see if emotes in list and place into sequence
                    #kinda a crappy workaround to remove the leading/trailing spaces in the list
                    sequence = []
                    for x in emotes:
                        if ':' in x:
                            sequence.append(x)
                            await message.channel.send(x)

                    for i in sequence:
                        await message.add_reaction(i)
                        
                except discord.errors.Forbidden:
                    pass
                except discord.errors.InvalidArgument:
                    pass
