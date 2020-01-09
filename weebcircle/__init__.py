from .weebcircle import weebcircle


def setup(bot):
    bot.add_cog(weebcircle(bot))
