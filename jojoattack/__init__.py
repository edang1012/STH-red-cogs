from .jojoattack import jojoattack


async def setup(bot):
    await bot.add_cog(jojoattack(bot))
