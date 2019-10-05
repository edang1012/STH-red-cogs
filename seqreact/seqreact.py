from redbot.core import commands

class seqreact(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def test(self, ctx, word, num):
        """Create a sequence of reactions to a keyword/phrase'
        Send the """
        guild = ctx.message.guild
        message = ctx.message
        #await ctx.send(word)
        #await ctx.send(num)
        await self.create_reaction_sequence(guild, message, word, num)
        
    async def create_reaction_sequence(self, guild, message, word, num):
        try:
            await message.channel.send('Word is {}, num is {}'.format(word, num))

        except (discord.errors.HTTPException, discord.errors.InvalidArgument):
            await message.channel.send("That's not an emoji I recognize. "
                                       "(might be custom!)")
