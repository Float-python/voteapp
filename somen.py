import discord
import random
from discord.ext import commands

import numpy as np
import json
import codecs
import asyncio
import time
class Test(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['おみくじ'])
    async def omikuji(self,ctx):
        if ctx.channel.id != 866965056544309248:
            return await ctx.send("ここではおみくじは出来ないぞ！")
        embed = discord.Embed(title="おみくじ", description=f"{ctx.author.mention}さんの今日の運勢は！", color=0x2ECC69)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name="▼結果▼ ", value=random.choice(('---**大吉**---\nおめでとう！どうだ？祈願でもしてみないか？？',
                                                            '---**中吉**---\n今日はいいことがありそうだな、旅人！',
                                                            '---**中吉**---\nたまには遠出してみるのも良いかもな、旅人！',
                                                            '---**中吉**---\n今日のラッキーメニューは「団子牛乳」だぞ！',
                                                            '---**小吉**---\n今日は思わぬ幸運に出会えるかも？',
                                                            '---**小吉**---\n今日のラッキーメニューは「ふわふわパンケーキ」だぞ！',
                                                            '---**小吉**---\n今日のラッキーメニューは「ムーンパイ」だぞ！',
                                                            '---**末吉**---\n今日も気をつけて冒険に出発だ！！',
                                                            '---**末吉**---\n今日のラッキーメニューは「活力にゃんこ飯」だぞ！',
                                                            '---**凶**---\n食料はちゃんと持ったか？周りをよく見て冒険しような！',
                                                            '---**凶**---\n冒険だ冒険！',
                                                            '---**大凶**---\n旅人、そんなに気を落とすなよ。こういう日もあるよな...',
                                                            '---**大凶**---\nお楽しみは、これからだ...')), inline=False)
        await ctx.reply(embed=embed)


    
    


    def character_prey(self):
        p = [0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.066, 0.126, 0.186, 0.246, 0.306, 0.366, 0.426, 0.486, 0.546, 0.606, 0.666, 0.726, 0.786, 0.846, 0.906, 0.966,1]
        ur = []
        for i in range(90):
            pref = p[i]
            x = np.random.choice(['5','4'], p=[pref,1-pref])
            if x == '5' or i == 89:
                    m = np.random.choice(['PU','not'],p=[0.5,0.5])
                    if m == 'PU':
                        return [i+1]
                    else: 
                        ur.append(i+1)
                        break
        for i in range(90):
            pref = p[i]
            x = np.random.choice(['5','4'], p=[pref,1-pref])
            if x == '5' or i == 89:
                ur.append(i+1)
                break
        return ur

    def wepon_prey(self):
        w = [0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.007, 0.077, 0.147, 0.217, 0.287, 0.357, 0.427, 0.497, 0.567, 0.637, 0.707, 0.777, 0.847, 0.917, 0.987, 1, 1, 1, 1]
        ur = []
        judge = False
        for i in range(80):
            pref = w[i]
            x = np.random.choice(['5','4'], p=[pref,1-pref])
            if x == '5' or i == 79:
                    m = np.random.choice(['meitei','PU','not'],p=[0.375,0.375,0.25])
                    print(m)
                    if m == 'meitei':
                        return [[i+1,'meitei']]
                    if m == 'not':
                        judge = True
                        ur.append([i+1,'not'])
                        break
                    else: 
                        ur.append([i+1,'PU'])
                        break
                    
        for i in range(80):
            pref = w[i]
            x = np.random.choice(['5','4'], p=[pref,1-pref])
            if x == '5' or i == 79:
                if judge:
                    m = np.random.choice(['meitei','PU'],p=[0.5,0.5])
                if not judge:
                    m = np.random.choice(['meitei','PU','not'],p=[0.375,0.375,0.25])
                if m == "meitei":
                    ur.append([i+1,m])
                    return ur
                else:
                    ur.append([i+1,m])
                    break

        for i in range(80):
            pref = w[i]
            x = np.random.choice(['5','4'], p=[pref,1-pref])
            if x == '5' or i == 79:
                ur.append([i+1,'meitei'])
                break
        return ur

    def read_json(self):
        with codecs.open('gacha.json', 'r',encoding='utf-8') as f:
            data = json.load(f)
        return data

    def write_json(self,data):
        with codecs.open('gacha.json', 'w',encoding='utf-8') as f:
            json.dump(data, f,indent=4,ensure_ascii=False)

    def add_count(self,uid):
        data = self.read_json()
        if str(uid) not in list(data.keys()):
            data[str(uid)] = 1
        else:
            data[str(uid)] += 1
        self.write_json(data)
        

    def check_id(self,uid):
        data = self.read_json()
        if str(uid) not in list(data.keys()):
            return True
        if data[str(uid)] >= 3:
            return False
        return True     

    
    @commands.command()
    async def gacha(self,ctx):
        if ctx.channel.id != 977849903470477323 and ctx.guild.id != 976735124735541279:
            return await ctx.send('ここでガチャシミュレーションはできないぞ')
        if not self.check_id(ctx.author.id):
            await ctx.message.delete()
            return await ctx.send(f'{ctx.author.mention}ガチャシミュレーターは1日3回までだぞ!')
        embed_s = discord.Embed(title='祈願シミュレーター',color=discord.Colour.green())
        embed_s.add_field(name='\U0001f9cd',value='`キャラクター祈願をシミュレートします。`',inline=False)
        embed_s.add_field(name='\U00002694',value='`武器祈願をシミュレートします。`',inline=False)
        embed_s.set_author(
            name=ctx.author.display_name,
            icon_url=ctx.author.avatar.url,
        )
        msg = await ctx.channel.send(content='▽ガチャタイプを選んでください',embed=embed_s)

        await msg.add_reaction('\U0001f9cd')
        await msg.add_reaction('\U00002694')

        def check(reaction,user):
            return user == ctx.author 


        
        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await msg.delete()
        else:
            for i in range(2):
                await msg.edit(content='`シミュレート中.`',suppress=True)
                time.sleep(0.3)
                await msg.edit(content='`シミュレート中..`',suppress=True)
                time.sleep(0.3)
                await msg.edit(content='`シミュレート中...`',suppress=True)
                time.sleep(0.3)
            if reaction.emoji == '\U0001f9cd':
                x = self.character_prey()
                if len(x) == 1:
                    embed = discord.Embed(title='キャラクター祈願結果',color=discord.Colour.green(),timestamp=ctx.message.created_at,)
                    embed.add_field(name='PU排出',value=f'`{x[0]}`連',inline=False)
                    embed.set_author(
                        name=ctx.author.display_name,
                        icon_url=ctx.author.avatar.url,
                        url=ctx.message.jump_url
                    )
                    embed.set_footer(
                        text=f'すり抜け:なし・消費原石:{x[0]*160}原石',
                        icon_url='https://cdn.discordapp.com/attachments/977069566926680064/977784004931616768/unknown.png'
                    )
                if len(x) == 2:
                    embed = discord.Embed(title='キャラクター祈願結果',color=discord.Colour.green(),timestamp=ctx.message.created_at)
                    embed.add_field(name='すりぬけ',value=f'`{x[0]}`連',inline=False)
                    embed.add_field(name='PU排出',value=f'`{x[0]+x[1]}`連',inline=False)
                    embed.set_author(
                        name=ctx.author.display_name,
                        icon_url=ctx.author.avatar.url,
                        url=ctx.message.jump_url
                    )
                    embed.set_footer(
                        text=f'すりぬけ:1回・消費原石{(x[0]+x[1])*160}gem',
                        icon_url='https://cdn.discordapp.com/attachments/977069566926680064/977784004931616768/unknown.png'
                    )
            if reaction.emoji=='\U00002694':
                x = self.wepon_prey()
                ct = 0
                d = {'not':'恒常武器','meitei':'命定武器','PU':'すり抜けPU武器'}

                embed = discord.Embed(title='武器祈願結果',color=discord.Colour.orange(),timestamp=ctx.message.created_at)
                for n in x:
                    ct += n[0]
                    embed .add_field(name=f'{ct}連目',value=f'結果:`{d[n[1]]}`(前回天井から{n[0]}連目)',inline=False)
                embed.set_author(
                    name=ctx.author.display_name,
                    icon_url=ctx.author.avatar.url,
                    url=ctx.message.jump_url
                )
                embed.set_footer(
                    text=f'すりぬけ:{len(x)-1}回・消費原石{ct*160}gem',
                    icon_url='https://cdn.discordapp.com/attachments/977069566926680064/977784004931616768/unknown.png'
                )

            await msg.delete()
            await ctx.send(embed=embed)
            self.add_count(ctx.author.id)

async def setup(bot):
    await bot.add_cog(Test(bot))
