import discord
from discord.ext import commands
permissoes = discord.Intents.default()
permissoes.message_content = True
permissoes.members = True

bot = commands.Bot(command_prefix="/", intents=permissoes)


@bot.command()
async def ola(ctx:commands.Context):
    print('Ola')
    usuario = ctx.author
    await ctx.reply(f'iai meu amigo {usuario.display_name}, {usuario.display_avatar}')


@bot.command()
async def quem_e_voce(ctx):
    await ctx.reply(f'Eu sou Carlos Alberto Alves Ribeiro, atualmente tenho 5 filhos e devo 10k de pensão')

@bot.command()
async def falar(ctx:commands.Context, *,falar):
    await ctx.send(falar)

@bot.event
async def on_ready():
    print('Estou Pronto!')

bot.run('MTMwMDExNzQyNDY4MjcwMDgwMQ.GQ1y73.1-566qdIA6qTxIpFguZjEvHGAnaX_5LoSU3x-A')
