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
        staff_state_ch = official_server.get_channel(700974856379826237)
        b_dict = discord.Embed(title='botが再起動しました!',description='Bumpに関する辞書です',colour=discord.Colour.blue())
        for g in self.bot.guilds:
            self.bump_time[g.id] = None
            b_dict.add_field(name='**辞書サーバー概要**',value=str(g.name)+'\n'+str(g.id))
            b_dict.add_field(name='value',value=str(bump_time[g.id]))
            await staff_state_ch.send(embed=b_dict)
        
        
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        official_server = self.bot.get_guild(700603441302732873)
        staff_state_ch = official_server.get_channel(700974856379826237)
        self.bump_time[guild.id]=None
        join_bump_dict = discord.Embed(title='新サーバー辞書通知',description='bumpに関する辞書です',colour=discord.Colour.red())
        join_bump_dict.add_field(name='新サーバー',value=str(guild.name)+'\n'+str(guild.id))
        join_bump_dict.add_field(name='value',value=str(bump_time[guild.id]))
        await staff_state_ch.send(embed=join_bump_dict)
                                 
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == 302050872383242240:
            if '表示順をアップしたよ' in message.embeds[0].description:
                await message.channel.send('わしはbumpを確認したぞ！')
                for time in range(120,0,-1):
                    self.bump_time[message.guild.id] = time
                    asyncio.sleep(60)
                    if self.bump_time[message.guild.id] == 5:
                        await message.channel.send('わしの腹時計があと5分！って言っとるぞ')
                    if self.bump_time[message.guild.id] == 0:
                        await message.channel.send('お腹がbumpを求めとる...')
            elif 'このサーバーを上げられるようになるまで' in message.embeds[0].description:
                await message.channel.send('わしの腹時計がまだbumpなんか入らないと言っておる')
              
                                
         
            
            
    
