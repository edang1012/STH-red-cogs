from .sthreact import sthreact


def setup(bot):
    bot.add_cog(sthreact(bot))
