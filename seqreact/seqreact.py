import os
import discord
import copy
from discord.ext import commands
from .utils.dataIO import dataIO
from __main__ import send_cmd_help


#test command to understand dataflow
@commands.command()
async def test(ctx, arg):
    """1Add an auto sequenced reaction to a word.
    Use the actual emoji and not the emoji name.
    Syntax: [p]addseq word
    """

    await ctx.send(arg)
