from discord.ext import commands
import os
import traceback
from Votecog import qa
from ActionCog import actioncommand
from HelpCog import helpcommands
bot = commands.Bot(command_prefix='*',help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']



@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_ready():
    print('login')
    
@bot.command()
async def code(ctx):
    code_embed = discord.Embed(title='Sorce code',description='suit:github  language:python',colour=discord.Colour.purple())
    code_embed.add_field(name='Code',value=['ameminn code']('https://github.com/Ameminn-python/voteapp'),inline=False)
    await ctx.send(embed=code_embed)
@bot.command()
async def invite(ctx):
    invite_embed = discord.Embed(title='Invite URL',description='this bot invite url',colour=discord.Colour.purple())
    invite_embed.add_field(name='Invite',value=['Invite Form']('https://github.com/Ameminn-python/voteapp'),inline=False)
    await ctx.send(embed=invite_embed)     

helpcommands = helpcommands()
bot.add_cog(qa(bot))
bot.add_cog(helpcommands)
bot.add_cog(actioncommand(bot))


bot.run(token)
