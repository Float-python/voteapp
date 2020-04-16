from discord.ext import commands
import os
import traceback
from Votecog import qa
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
    await ctx.send('pls check this URL')
    await ctx.send('https://github.com/Ameminn-python/voteapp')
    
@bot.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/api/oauth2/authorize?client_id=686677905115578403&permissions=8&scope=bot')

helpcommands = helpcommands()
bot.add_cog(qa(bot))
bot.add_cog(helpcommands)


bot.run(token)
