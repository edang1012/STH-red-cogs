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


    @commands.command()
    async def test(self, ctx, word, emoji):
        """Create a sequence of reactions to a keyword/phrase'
        Usage:  pass a keyword or keyphrase(in quotations) to <word>
                pass an emoji or emojis (in quotations) to <emoji>
                
                the order of emojis sent will be the sequence"""
        
        guild = ctx.message.guild
        message = ctx.message
        await self.create_reaction_sequence(guild, message, word, emoji)
        
    @commands.command()
    async def test1(self, ctx, word, emoji):
        """Delete an auto reaction to a word"""
        guild = ctx.message.guild
        message = ctx.message
        await self.remove_reaction_sequence(guild, word, emoji, message)
      
        
    async def create_reaction_sequence(self, guild, message, word, emoji):
        #split emoji list into string array 
        #emotes = emoji.split(" ")

        #check to see if emotes in list and place into sequence
        #kinda a crappy workaround to remove the leading/trailing spaces in the list
        #sequence = []
        #for x in emotes:
        #    if ':' in x:
        #        sequence.append(x)
                #await message.channel.send(x)

        #for i in sequence:
        #    await message.channel.send(i)
            
        try:
            # Use the reaction to see if it's valid
            #await message.add_reaction(emoji)
            emoji = str(emoji)
            reactions = await self.conf.guild(guild).reactions()
            
            if emoji in reactions:
                if word.lower() in reactions[emoji]:
                    await message.channel.send("This smart reaction already exists.")
                    return
                reactions[emoji].append(word.lower())
            else:
                reactions[emoji] = [word.lower()]
            await self.conf.guild(guild).reactions.set(reactions)
            await message.channel.send("Successfully added this reaction.")

        except (discord.errors.HTTPException, discord.errors.InvalidArgument):
            await message.channel.send("That's not an emoji I recognize. "
                                       "(might be custom!)")
            
            
    async def remove_reaction_sequence(self, guild, word, emoji, message):
        try:
            emoji = str(emoji)
            reactions = await self.conf.guild(guild).reactions()
            if emoji in reactions:
                if word.lower() in reactions[emoji]:
                    reactions[emoji].remove(word.lower())
                    await self.conf.guild(guild).reactions.set(reactions)
                    await message.channel.send("Removed this smart reaction.")
                else:
                    await message.channel.send("That emoji is not used as a reaction "
                                               "for that word.")
            else:
                await message.channel.send("There are no smart reactions which use "
                                           "this emoji.")

        except (discord.errors.HTTPException, discord.errors.InvalidArgument):
            await message.channel.send("That's not an emoji I recognize. "
                               "(might be custom!)")
