from discord.ext import commands
import discord
import os
import traceback
from Votecog import qa
from ActionCog import actioncommand
from HelpCog import helpcommands
from Admin import admin
from bump import Bump
from Surpport import Surpport
import time
bot = commands.Bot(command_prefix='*',help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']



@bot.event
async def on_command_error(ctx, error):
    official_server = bot.get_guild(700603441302732873)
    error_ch = official_server.get_channel(700638984425963560)
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    error_embed = discord.Embed(title='エラーが発生しました',description=str(ctx.guild.id),color=discord.Colour.red())
    error_embed.add_field(name='エラー原因参考',value='```1.引数を指定してない\n2.botに権限がない\n3.使い方が間違っている```\n上記で解決しない場合公式サーバーまでスクショをお願いします',inline=False)
    error_embed.add_field(name='Traceback',value=error_msg,inline=False)
    await ctx.send(embed=error_embed)
    await error_ch.send(embed=error_embed)


@bot.event
async def on_ready():
    login_t = time.ctime()
    cnvtime = time.strptime(login_t)
    login_time = time.strftime("%Y/%m/%d %H:%M", cnvtime)
    official = bot.get_guild(700603441302732873)
    login_ch = official.get_channel(700638466807169065)
    state_ch = official.get_channel(700613819939946546)
    login_embed = discord.Embed(title='Botが復帰しました!',description='LOGINED',colour=discord.Colour.green())
    login_embed.add_field(name='ステータス',value='login time'+str(login_time)+'succsess')
    await login_ch.send(embed=login_embed)
    await state_ch.send(embed=login_embed)
    
    print('login')
    
@bot.command()
async def code(ctx):
    code_embed = discord.Embed(title='Sorce code',description='suit:github  language:python',colour=discord.Colour.purple())
    code_embed.add_field(name='Code',value='[ameminn code](https://github.com/Ameminn-python/voteapp)',inline=False)
    await ctx.send(embed=code_embed)
@bot.command()
async def invite(ctx):
    invite_embed = discord.Embed(title='Invite URL',description='this bot invite url',colour=discord.Colour.purple())
    invite_embed.add_field(name='Invite',value='[Invite Form](https://discordapp.com/api/oauth2/authorize?client_id=686677905115578403&permissions=8&scope=bot)',inline=False)
    await ctx.send(embed=invite_embed)     

helpcommands = helpcommands()
bot.add_cog(qa(bot))
bot.add_cog(helpcommands)
bot.add_cog(actioncommand(bot))
bot.add_cog(admin(bot))
bot.add_cog(Bump(bot))
bot.add_cog(Surpport(bot))


bot.run(token)
