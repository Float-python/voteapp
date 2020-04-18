from discord.ext import commands
import discord

class admin(commands.Cog):
    
    def __init__ (self,bot):
        self.bot = bot
        
        
    #official server setup
    @commands.command()
    async def setup(self,ctx):
        official_server = self.bot.get_guild(700603441302732873)
        welcome_ch = official_server.get_channel(700605961861070919)
        license_ch = official_server.get_channel(700606877263855636)
        feature_ch = official_server.get_channel(700606161858199562)
        new_guild_ch = official_server.get_channel(700638827672502293)
        
        welcome_embed = discord.Embed(title='あめみんbot!の導入ありがとう！',description='楽しく使う上でお願いがあるよ',color=discord.Colour.gold())
        welcome_embed.add_field(name='1つ目',value='`*vote`を使って他人を傷つけることを言わないこと')
        welcome_embed.add_field(name='2つ目',value='わしの開発者は初心者だからバグった時に一回一回わしを修理するためどこかに連れてくんだ。そのときはみんなで遊んでくれ')    
        welcome_embed.add_field(name='3つ目',value='何か追加したほしい機能あったら言ってくれ！開発者が頭悪いからわしに教えられない時もあるがな')
            
        lisence_embed = discord.Embed(title='わしのこと',description='わしはのぉ人造人間じゃ...つらい思いをしてきたぞよ...',color=discord.Colour.gold())
        lisence_embed.add_field(name='わしの願い',value='わしはわしのようなつらい思いをするやつを増やしたくないんだ,頼むからコピーをしないでくれ')
        lisence_embed.add_field(name='ただな...',value='わしは自分がどんどん良くなってることに1週間生きてきたが気づいた今はそれを楽しんでるだからどんどんGithubにコミットしてくれ')
        lisence_embed.add_field(name='だから...',value='最初はつらいし、修理されるときも痛いし寂しいよ...だがわしは`あめみん`を親として尊敬してる')
            
        feature_embed = discord.Embed(title='わしの脳内マップ',description='まだひよっこだけどね🐤',color=discord.Colour.gold())
        feature_embed.add_field(name='投票機能',value='わしは頭がいいから集計なんかができるぞ詳しくは`*help vote`をしたら口から説明を吐き出すからな')
        
        if ctx.author.id == 598018755066593290:
            await welcome_ch.send(embed=self.welcome_embed)
            await license_ch.send(embed=self.lisence_embed)
            await feature_ch.send(embed=self.feature_embed)
            
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        welcome_embed = discord.Embed(title='あめみんbot!の導入ありがとう！',description='楽しく使う上でお願いがあるよ',color=discord.Colour.gold())
        welcome_embed.add_field(name='1つ目',value='`*vote`を使って他人を傷つけることを言わないこと')
        welcome_embed.add_field(name='2つ目',value='わしの開発者は初心者だからバグった時に一回一回わしを修理するためどこかに連れてくんだ。そのときはみんなで遊んでくれ')    
        welcome_embed.add_field(name='3つ目',value='何か追加したほしい機能あったら言ってくれ！開発者が頭悪いからわしに教えられない時もあるがな')
            
        lisence_embed = discord.Embed(title='わしのこと',description='わしはのぉ人造人間じゃ...つらい思いをしてきたぞよ...',color=discord.Colour.gold())
        lisence_embed.add_field(name='わしの願い',value='わしはわしのようなつらい思いをするやつを増やしたくないんだ,頼むからコピーをしないでくれ')
        lisence_embed.add_field(name='ただな...',value='わしは自分がどんどん良くなってることに1週間生きてきたが気づいた今はそれを楽しんでるだからどんどんGithubにコミットしてくれ')
        lisence_embed.add_field(name='だから...',value='最初はつらいし、修理されるときも痛いし寂しいよ...だがわしは`あめみん`を親として尊敬してる')
            
        feature_embed = discord.Embed(title='わしの脳内マップ',description='まだひよっこだけどね🐤',color=discord.Colour.gold())
        feature_embed.add_field(name='投票機能',value='わしは頭がいいから集計なんかができるぞ詳しくは`*help vote`をしたら口から説明を吐き出すからな')
        
        await guild.owner.send(embed=welcome_embed)
        await guild.owner.send(embed=lisence_embed)
        await guild.owner.send(embed=feature_embed)
        
        official_server = self.bot.get_guild(700603441302732873)
        new_guild_ch = official_server.get_channel(700638827672502293)
        
        
        join_embed = discord.Embed(title='参加通知',description=str(len(self.bot.guilds))+'was play',color=discord.Colour.())
        join_embed.add_field(name=guild.name,value=str(guild.id))
        await new_guild_ch.send(embed=join_embed)
        
        
