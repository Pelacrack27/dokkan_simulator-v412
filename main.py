import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
	await client.change_presence(
	    status=discord.Status.online,
	    activity=discord.Game(name="!ayuda - summons disponibles | v4.1.8"))
	print("Estoy funcionando!")
	print(client.user)


@client.command()
async def ping(ctx):
	ping = client.latency * 1000
	await ctx.send(f'Mi ping es {ping} milisegundos')


@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")


@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.environ["DISCORD_TOKEN"])
