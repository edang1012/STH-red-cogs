from .sthcommands import sthcommands


def setup(bot):
    bot.add_cog(sthcommands(bot))
