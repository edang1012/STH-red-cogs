from .sthreact import sthreact


async def setup(bot):
    await bot.add_cog(sthreact(bot))
