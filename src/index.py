from unittest.util import _MAX_LENGTH
import discord
import random
from discord.ext import commands

comandos = ["c", "cambiar_caras", "v", "valor_dado", "d", "dado", "h"]
prefix_discord = '#'
caras_dado = 6
bot = commands.Bot(command_prefix=prefix_discord, description="Lanza tus dados!")

@bot.check
def check_commands(ctx):
    return True

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(name="Dado", type=1))
    print("El dado está listo!")

@bot.command()
async def cambiar_caras(ctx, numcaras: int):
    global caras_dado
    if numcaras == 0:
        await ctx.send("El dado no es descarado 🤨")
        return
    if numcaras < 0:
        await ctx.send("Really? 🤣")
        return
    if numcaras == 1:
        await ctx.send("Ponele voluntad 🤡")
        return
    if numcaras == caras_dado:
        await ctx.send("Altoque 👍")
        return
    caras_dado = numcaras
    await ctx.send(f"🎲El dado cambio a {caras_dado} caras🎲")

@bot.command()
async def c(ctx, numcaras: int):
    await cambiar_caras(ctx, numcaras)

@bot.command()
async def h(ctx):
    embed = discord.Embed(title="Ayuda", description="Comandos del bot de dado",color=discord.Color.blue())
    embed.add_field(name=f"{prefix_discord}c num o {prefix_discord}cambiar_caras num", value=f"Cambia el número de caras del dado a num. Ej {prefix_discord}c 6.")
    embed.add_field(name=f"{prefix_discord}v o {prefix_discord}valor_dado", value="Muestra las caras que tiene el dado actualmente.")
    embed.add_field(name=f"{prefix_discord}d o {prefix_discord}dado", value="Lanza el dado.")
    embed.add_field(name=f"{prefix_discord}h", value="Muestra este mensaje de ayuda.")

    await ctx.send(embed=embed)

@bot.command()
async def dado(ctx):
    _random = random.randint(1, caras_dado)
    await ctx.send(f"🎲 = {_random}")

@bot.command()
async def d(ctx):
    await dado(ctx)

@bot.command()
async def valor_dado(ctx):
    await ctx.send(f"🎲El dado tiene {caras_dado} caras🎲")

@bot.command()
async def v(ctx):
    await valor_dado(ctx)

bot.run("") # Insertar token aqui