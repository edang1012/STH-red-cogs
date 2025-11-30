from .wat import Wat


async def setup(bot):
    await bot.add_cog(Wat(bot))
