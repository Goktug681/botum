import os
import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def atik(ctx,atik_turu=None):
    if atik_turu=="plastik":
        await ctx.send("Sarı kutuya atmalısın")
    elif atik_turu=="kağıt":
        await ctx.send("Mavi kutuya atmalısın")
    elif atik_turu=="cam":
        await ctx.send("Yeşil kutuya atmalısın")
    else:
        await ctx.send("Bu atık türü hakkında bilgimiz yooook!")             

@bot.command()
async def ayrisma(ctx,ayrisma_zamani=None):
    if ayrisma_zamani=="plastik_şişe":
        await ctx.send("Plastik şişeler 450 yılda ayrışır")
    elif ayrisma_zamani=="bebek_bezi":
        await ctx.send("Bebek bezleri 550 yılda ayrışır")
    elif ayrisma_zamani=="elma_çöpü":
        await ctx.send("Elma çöpü 2 ayda ayrışır") 
    elif ayrisma_zamani=="aliminyum_kutular":
        await ctx.send("Aliminyum kutular 200-300 yılda ayrışır")
    elif ayrisma_zamani=="çöp_poşetleri":
        await ctx.send("Çöp poşetleri en az 1000 yılda ayrışır")
    else:
        await ctx.send("Bununla ilgili bilgi yoook!")                   


@bot.command()
async def mem(ctx):
    mems = os.listdir("imeges")
    choice = random.choice(mems)
    with open(f'imeges/{choice}', 'rb') as f:
        picture = discord.File(f)
        
        await ctx.send(file=picture)    # bu dosyayı parametre olarak gönderebiliriz

bot.run("")
