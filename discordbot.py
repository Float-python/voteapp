from discord.ext import commands
import os
import traceback
from Votecog import qa
from HelpCog import helpcommands
bot = commands.Bot(command_prefix='*')
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
async def code():
    await ctx.send('pls check this URL')
    await ctx.send('https://github.com/Ameminn-python/voteapp')


bot.add_cog(qa(bot))
bot.add_cog(helpcommands)


bot.run(token)
