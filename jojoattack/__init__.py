from .jojoattack import jojoattack


def setup(bot):
    bot.add_cog(jojoattack(bot))
