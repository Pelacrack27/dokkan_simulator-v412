import discord
from discord.ext import commands

class Ayuda(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("ayuda online")

  #Comandos del bot
  @commands.command()
  async def ayuda(self, ctx):
    embed=discord.Embed(title="Ayuda",  description="A continuación se muestran los multisummons diponibles", color=discord.Color.blue())
    embed.set_author(name=ctx.author.display_name,  icon_url=ctx.author.avatar_url)
    embed.add_field(name="!probs", value="Comprueba las probabilidades de los multisummons", inline=False)
    embed.add_field(name="!multigoku", value="Multisummon de goku dokkan fest", inline=False)
    embed.add_field(name="!multicell", value="Multisummon de cell dokkan fest", inline=False)
    embed.add_field(name="!multizdokkan", value="Multisummon de Extreme Z dokkan fest", inline=False)
    embed.add_field(name="!multibuu", value="Multisummon de majin buu saga", inline=False)
    embed.add_field(name="!multilegendary", value="Multisummon de Legendary Summon", inline=False)
    embed.add_field(name="!multilrcell", value="Multisummon de Legendary Summon Cell EZA (Sale el 24 de Mayo)", inline=False)
    embed.set_footer(text="Muchas gracias por usar el bot!")
    await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Ayuda(client))