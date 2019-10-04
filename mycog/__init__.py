"""Package for mycog cog."""
from .mycog import sigh

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(sigh(bot))
