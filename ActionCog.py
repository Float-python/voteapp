import discord
from discord.ext import commands

class actioncommand(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        
    
    @commands.command()
    async def notice(self,ctx,*,content=None):
        if ctx.author.id == 598018755066593290:
            if content is not None:
                for g in self.bot.guilds:
                    if g.system_channel is None:
                        try:
                            await g.owner.send(content)
                        except discord.errors.Forbidden:
                            pass
                    if g.system_channel is not None:
                        try:
                            await g.system_channel.send(content)
                        except discord.errors.Forbidden:
                            pass
            if content is None:
                await ctx.send('argument is not designneire')
        else:
            await ctx.send('You have not adminstar')
            
                
                    
                        
    
