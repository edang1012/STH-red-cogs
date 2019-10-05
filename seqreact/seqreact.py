from redbot.core import commands

class seqreact(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def test(self, ctx, word, num):
        """This does stuff!"""
        # Your code will go here
        await ctx.send(word)
        await ctx.send(num)
