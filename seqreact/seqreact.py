from redbot.core import commands

class seqreact(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def test(self, ctx, word, emoji):
        
        """Create a sequence of reactions to a keyword/phrase'
        Usage:  pass a keyword or keyphrase(in quotations) to <word>
                pass an emoji or emojis (in quotations) to <emoji>
                
                the order of emojis sent will be the sequence"""
        
        guild = ctx.message.guild
        message = ctx.message
        await self.create_reaction_sequence(guild, message, word, emoji)
        
        
    async def create_reaction_sequence(self, guild, message, word, emoji):
        try:
            emotes = emoji.split(" ")
            
            for x in emotes:
                if ' ' not in x:
                    await message.channel.send(x)

            #await message.channel.send('Word is {}, num is {}'.format(word, emoji))

        except (discord.errors.HTTPException, discord.errors.InvalidArgument):
            await message.channel.send("That's not an emoji I recognize. "
                                       "(might be custom!)")
