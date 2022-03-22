from discord.ext import commands
from os import getenv
import traceback
import random

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def slot(ctx):
    slot_list = ['n1', 'n2', 'n3', 'n4']
    A = random.choixe(slot_list)
    B = random.choixe(slot_list)
    C = random.choixe(slot_list)
    D = random.choixe(slot_list)
    await ctx.send("%s%s%s%s", (A, B, C, D))
    
    


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
