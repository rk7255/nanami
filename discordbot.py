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
    slot_list = ["<:n1:952222321538654339>", "<:n2:952222338957606923>", "<:n3:952222351586631740>", "<:n4:952222370154811452>"]
    list_shuffle = random.sample(slot_list, 4)
    A = list_shuffle[0]
    B = list_shuffle[1]
    C = list_shuffle[2]
    D = list_shuffle[3]
    
    s = A + B + '\n' + C + D
    correct = "<:n1:952222321538654339>" + "<:n2:952222338957606923>" + '\n' + "<:n3:952222351586631740>" + "<:n4:952222370154811452>"
    name = message.author.id
    await ctx.send(name)
    await ctx.send(s)
    if s == correct :
            await ctx.send("Congrats!!!")
            
@bot.command()
async def baka(ctx):
    slot_list = ["<:nr1:980975270863446016>", "<:nr2:980975382884933672>", "<:nr3:980975433992523847>", "<:nr4:980975462018850866>"]
    list_shuffle = random.sample(slot_list, 4)
    A = list_shuffle[0]
    B = list_shuffle[1]
    C = list_shuffle[2]
    D = list_shuffle[3]
    
    s = A + B + '\n' + C + D
    correct = "<:nr1:980975270863446016>" + "<:nr2:980975382884933672>" + '\n' + "<:nr3:980975433992523847>" + "<:nr4:980975462018850866>"
    await ctx.send(s)
    if s == correct :
            await ctx.send("バ〜〜〜カ！！！")
       
      
            
    
token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
