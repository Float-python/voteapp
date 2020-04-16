import discord
from discord.ext import commands

class actioncommand(commands.Cog):
    
    def __init__(self):
        pass
        
    
    @commands.command()
    async def hello(ctx):
        await ctx.send('hello')
    
