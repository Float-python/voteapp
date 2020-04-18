from discord.ext import commands
import discord
import asyncio

class Bump(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        self.bump_time = dict()
        
    @commands.Cog.listener()
    async def on_ready(self):
        official_server = self.bot.get_guild(700603441302732873)
        
        b_dict = dscord.Embed(title='botが再起動しました!',description='Bumpに関する辞書です',colour=discord.Colour.blue())
        for g in self.bot.guilds:
            self.bump[g.id] = None
            b_dict.add_field(name='**辞書サーバー概要**',value=str(g.name)+'\n'+str(g.id))
            await 
            
            
            
    
