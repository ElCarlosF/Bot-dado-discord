from unicodedata import name
import discord
import random
from discord.ext import commands

comandos = ["c", "cambiar_caras", "v", "valor_dado", "d", "dado", "h", "C", "cantidad_dados", "V", "valor_cant_dados"]
prefix_discord = '#'
caras_dado = 6
numeros_datos = 1
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
        await ctx.send("🎲 no es descarado 🤨")
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
    await ctx.send(f"🎲Cantidad de caras cambio a {caras_dado}🎲")

@bot.command()
async def c(ctx, numcaras: int):
    await cambiar_caras(ctx, numcaras)

@bot.command()
async def h(ctx):
    embed = discord.Embed(title="Ayuda", description="Comandos del bot de dado",color=discord.Color.blue())
    embed.add_field(name=f"{prefix_discord}c num o {prefix_discord}cambiar_caras num", value=f"Cambia el número de caras de los dados a num. Ej {prefix_discord}c 6.")
    embed.add_field(name=f"{prefix_discord}v o {prefix_discord}valor_dado", value="Muestra las caras que tiene los dados actualmente.")
    embed.add_field(name=f"{prefix_discord}d o {prefix_discord}dado", value="Lanza el o los dados.")
    embed.add_field(name=f"{prefix_discord}C num o {prefix_discord}cantidad_dados num", value="Cambias la cantidad de dados a num.")
    embed.add_field(name=f"{prefix_discord}V o {prefix_discord}valor_cant_dados", value="Muestra cuando dados hay actualmente.")
    embed.add_field(name=f"{prefix_discord}h", value="Muestra este mensaje de ayuda.")

    await ctx.send(embed=embed)

@bot.command()
async def dado(ctx):
    mensaje = ""
    total = 0
    _random = random.randint(1, caras_dado)
    if numeros_datos == 1:
        await ctx.send(f"🎲: {_random}")
    else:
        mensaje = f"[🎲: {_random}"
        total = _random
        for i in range(1, numeros_datos):
            _random = random.randint(1, caras_dado)
            mensaje += f", 🎲: {_random}"
            total += _random
        mensaje += f"] = {total}" 
        await ctx.send(mensaje)

@bot.command()
async def d(ctx):
    await dado(ctx)

@bot.command()
async def valor_dado(ctx):
    await ctx.send(f"🎲El o los dados tienen {caras_dado} caras🎲")

@bot.command()
async def v(ctx):
    await valor_dado(ctx)

@bot.command()
async def cantidad_dados(ctx, n_dados: int):
    global numeros_datos
    if n_dados < 1:
        await ctx.send(f"Debe existir al menos un 🎲")
    elif n_dados == numeros_datos:
        await ctx.send(f"Ya hay {numeros_datos} 🎲")
    else:
        numeros_datos = n_dados
        await ctx.send(f"Ahora hay {numeros_datos} 🎲")

@bot.command()
async def C(ctx, n_dados: int):
    await cantidad_dados(ctx, n_dados)

@bot.command()
async def valor_cant_dados(ctx):
    await ctx.send(f"Hay {numeros_datos} 🎲")

@bot.command()
async def V(ctx):
    await valor_cant_dados(ctx)

bot.run("") # Insertar token aqui