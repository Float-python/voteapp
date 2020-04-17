import discord
from discord.ext import commands

class qa(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.Question = dict()
        self.do_q = dict()
        self.adm = dict()
        self.reaction_message = dict()
        self.asr_channel = dict()
        
    @commands.Cog.listener()
    async def on_ready(self):
        for g in self.bot.guilds:
            self.Question[g.id] = None
            self.do_q[g.id]=False
            self.adm[g.id]=None
            self.reaction_message[g.id] = None
            self.asr_channel[g.id] = None

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        self.Question[guild.id] = None
        self.do_q[guild.id]=None
        self.adm[guild.id]=None
        self.reaction_message[guild.id] = None
        self.asr_channel[guild.id] = None
            
        
   

    


    @commands.command()
    async def vote(self,ctx,*,subject=None):
        print(ctx.guild.id)
        print(self.Question)
        if subject is None:
            await ctx.send('わしの*voteをまちがえるな！もし助けが必要なら*help voteをするとわしの口から説明書が出てくるよ')
            return a
        if ctx.guild.id in self.Question:
            if self.Question[ctx.guild.id] is None:
                self.adm[ctx.guild.id] = ctx.author
                self.Question[ctx.guild.id] = subject
                await ctx.send('わしは頭がいいから質問を覚えたぞ！ノリで答えを4つまで覚えてやる*asr 答え①/答え② って感じで教えてくれ')
            else:
                await ctx.send('吾輩は頭が悪いからな一個しか覚えられんｗすまんのぉ...')
        else:
            await ctx.send('う、うわぁ体が...変になっちゃった...公式サーバーでこれを教えてね(votr:dictError)')
        
    @commands.command()
    async def asr(self,ctx,a):
        if a is None:
            await ctx.send('*asrミスってね？ｗ 使い方は*help voteを使えばわしのテンションは下がるけど教えてあげよう！')
        if ctx.guild.id in self.Question and a is not None:
            if self.Question[ctx.guild.id] is not None:
                self.asr_channel[ctx.guild.id] = ctx.channel
                answer= a
                answer_list = answer.split('/')
                num = len(answer_list)
                emoji=list()
                if num >= 1:
                    emoji.append('1️⃣')
                if num >= 2:
                    emoji.append('2️⃣')
                if num >= 3:
                    emoji.append('3️⃣')
                if num >= 4:
                    emoji.append('4️⃣')
                q_embed = discord.Embed(title='ほーれアンケートだぞ',description=(str(self.Question[ctx.guild.id])),colour=discord.Colour.green())
                for (l_answer_num,l_answer) in zip(answer_list,emoji):
                    q_embed.add_field(name=(l_answer_num),value=(l_answer),inline=False)
                self.reaction_message[ctx.guild.id] = await ctx.send(embed=q_embed)
                for reaction_emoji in emoji:
                    await self.reaction_message[ctx.guild.id].add_reaction(reaction_emoji)
                self.do_q[ctx.guild.id] = True
                

    @commands.command()
    async def fin(self,ctx):
        print(self.asr_channel)
        if self.do_q[ctx.guild.id] == True:
            f_re_msg = await self.asr_channel[ctx.guild.id].fetch_message(self.reaction_message[ctx.guild.id].id)
            result_e = discord.Embed(title='集計しといたぞ！',description=(f_re_msg.jump_url),colour=discord.Colour.magenta())
            for reaction in f_re_msg.reactions:
                result_e.add_field(name=str(reaction.emoji),value='この絵文字が追加された数は'+str((reaction.count)-1)+'票だったぞー')
            await ctx.send(embed=result_e)
            self.do_q[ctx.guild.id] = False
            self.Question[ctx.guild.id] = None
        elif self.do_q[ctx.guild.id] == False:
            await ctx.send('え、まだ...質問してなくないか？w *voteで質問してくれ！')
            self.Question[ctx.guild.id] = None
        else:
            self.do_q[ctx.guild.id] = False
            self.Question[ctx.guild.id] = None

            

    @commands.command()
    async def update(self,ctx):
        if ctx.author.id == 598018755066593290:
            for server in self.bot.guilds:
                if server.id != 696446597105713362:
                    if server.id != 700603441302732873:
                        if server.system_channel is None:
                            try:
                                await server.owner.send('なんかあめみんさんがわしを修理するっつって束縛してるんだもうすぐ消えるかも')
                            except discord.errors.Forbidden:
                                pass
                        if server.system_channel is not None:
                            try:
                                await server.owner.send('なんかあめみんさんがわしを修理するっつって束縛してるんだもうすぐ消えるかも')
                            except discord.errors.Forbidden:
                                pass
                    else:
                        g = self.bot.get_guild(server.id)
                        ch = g.get_channel(700609514931748894)
                        await ch.send('そろそろダウンタイムが始まります！')
                            
    
