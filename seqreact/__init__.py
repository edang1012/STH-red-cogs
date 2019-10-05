from .seqreact import seqreact

def setup(bot):
    bot.add_cog(seqreact(bot))
