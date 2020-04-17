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
            await ctx.send('The *vote is used incorrectly pls check help command(*help <feature>) ')
            return a
        if ctx.guild.id in self.Question:
            if self.Question[ctx.guild.id] is None:
                self.adm[ctx.guild.id] = ctx.author
                self.Question[ctx.guild.id] = subject
                await ctx.send('Answer pls startswith *asr answer1/answer2/an...(Max:4)')
            else:
                await ctx.send('You have any question in guild')
        else:
            await ctx.send('dict Error(Vote): pls feedback to ameminn')
        
    @commands.command()
    async def asr(self,ctx,a):
        if a is None:
            await ctx.send('The *asr is used incorrectly pls check help command(*help <feature>)')
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
                q_embed = discord.Embed(title='アンケート',description=(str(self.Question[ctx.guild.id])),colour=discord.Colour.green())
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
            result_e = discord.Embed(title='Result form',description=(f_re_msg.jump_url),colour=discord.Colour.magenta())
            for reaction in f_re_msg.reactions:
                result_e.add_field(name=str(reaction.emoji),value='The number of times this reaction was done'+str((reaction.count)-1))
            await ctx.send(embed=result_e)
            self.do_q[ctx.guild.id] = False
            self.Question[ctx.guild.id] = None
        elif self.do_q[ctx.guild.id] == False:
            await ctx.send('You have not yet added votes')
            self.Question[ctx.guild.id] = None
        else:
            self.do_q[ctx.guild.id] = False
            self.Question[ctx.guild.id] = None

    @commands.command()
    async def state(self,ctx,page):
        if ctx.author.id == 598018755066593290:
            

    @commands.command()
    async def update(self,ctx):
        if ctx.author.id == 598018755066593290:
            for server in self.bot.guilds:
                if server.system_channel is None:
                    await server.owner.send('bot downtime will comming soon. so this bot will stop')
                if server.system_channel is not None:
                    await server.system_channel.send('bot downtime will comming soon. so this bot will stop')
                    
    
