import discord
from discord.ext import commands

class Surpport(commands.Cog):
    
    def __init__(self,bot):
        self.bot = bot
        

    
    @commands.command()
    async def connect(self,ctx,*,msg):
        official = self.bot.get_guild(700603441302732873)
        help_category = official.get_channel(701966039558389911)
        msg_guild = ctx.guild
        spt_ch = None
        if msg_guild != official:
            for check_ch in help_category.channels:
                if check_ch.name == str(msg_guild.id):
                    spt_ch = check_ch
            if spt_ch == None:
                spt_ch = await help_category.create_text_channel(name=str(msg_guild.id))
                new_sp_em = discord.Embed(title=str(msg_guild.name),description=(ctx.author.name+'が作成しました'),colour=discord.Colour.red())
                new_sp_em.add_field(name='お問い合わせID',value='`'+str(msg_guild.id)+'`')
                await spt_ch.send(new_sp_em)
                cnt_emb = dicord.Embed(title=str(ctx.author.name)+'さんからメッセージ',description=None,colour=discord.Colour.blue())
                cnt_emb.add_field(name='内容',value='```'+str(msg)+'```')
                await spt_ch.send(embed=cnt_emb)
                try:
                    a_ch = await msg_guild.create_text_channel(name='あめみんhelp')
                    await a_ch.send()
                except discord.errors.Forbidden:
                    except_emb = discord.Embed(title='エラーが発生したよ!!',description='チャンネルの作成に失敗しました',colour=discord.Colour.red())
                    except_emb.add_field(name='サポートチャンネルの作成に失敗しました',value='`権限設定`を確認してください。')
                    await ctx.send(embed=except_emb)
                    await spt_ch.send('相手側でサポートチャンネルの作成に失敗してしまいました')
            else:
                cnt_emb = discord.Embed(title=str(ctx.author.name)+'さんからメッセージ',description=None,colour=discord.Colour.blue())
                cnt_emb.add_field(name='内容',value='```'+str(msg)+'```')
                await spt_ch.send(embed=cnt_emb)
                await ctx.send('無事にメッセージが届きました')
        else:
            msg_channel = int(ctx.channel.name)
            ans_guild = self.bot.get_(msg_channel)
            ans_ch = None
            for ch_check in ans_guild.channels:
                if ch_check.name == 'あめみんhelp':
                    ans_ch = ch_check
            if ans_ch == None:
                ans_embed = discord.Embed(title='サポートが来ました',description='helpチャンネルを確認できませんでしたのでDM失礼いたします。',colour=discord.Colour.red())
                ans_embed.add_field(name=str(ctx.author.name)+'からのサポート',value='```'+str(msg)+'```')
                await ans_guild.owner.send(embed=ans_embed)
                await ctx.send('無事にメッセージが届きました(オーナーDM)')
            else:
                ans_embed = discord.Embed(title='サポートが来ました',description='あめみんhelpチャンネルに送信します',colour=discord.Colour.red())
                ans_embed.add_field(name=str(ctx.author.name)+'からのサポート',value='```'+str(msg)+'```')
                await ans_ch.send(embed=ans_embed)
                await ctx.send('無事にメッセージが届きました(helpチャンネル)')




            


