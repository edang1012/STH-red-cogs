from .sthcommands import sthcommands


async def setup(bot):
    await bot.add_cog(sthcommands(bot))
