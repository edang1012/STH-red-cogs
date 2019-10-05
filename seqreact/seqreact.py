from redbot.core import commands

class seqreact(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def test(self, ctx, word, emoji):
        
        """Create a sequence of reactions to a keyword/phrase'
        Usage:  pass a keyword or keyphrase(in quotations) to <word>
                pass an emoji or emojis (in quotations) to <emoji>
                
                the order of emojis sent will be the sequence"""
        
        guild = ctx.message.guild
        message = ctx.message
        await self.create_reaction_sequence(guild, message, word, emoji)
        
        
    async def create_reaction_sequence(self, guild, message, word, emoji):
        try:
            #split emoji list into string array 
            emotes = emoji.split(" ")
            
            #check to see if 
            for x in emotes:
                if ':' in x:
                    sequence.append(x)
                    #await message.channel.send(x)
                    
            for i in sequence:
                await message.channel.send(i)
