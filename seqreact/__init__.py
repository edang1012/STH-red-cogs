from .seqreact import seqreact

async def setup(bot):
    await bot.add_cog(seqreact(bot))
