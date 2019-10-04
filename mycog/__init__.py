"""Package for mycog cog."""
from .mycog import mycog


def setup(bot):
    """Load RemindMe cog."""
    bot.add_cog(mycog(bot))
