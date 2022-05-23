import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_goku2 = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/73/Card_1024280_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426040336",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/ae/Card_1024310_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426060801",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/20/Card_1017880_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035025",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/31/Card_1022640_thumb.png/revision/latest/scale-to-width-down/120?cb=20211230080241",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/bf/Card_1021320_thumb.png/revision/latest/scale-to-width-down/120?cb=20210331131538",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/98/Card_1019580_thumb.png/revision/latest/scale-to-width-down/120?cb=20201105071645",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c3/Card_1021800_thumb.png/revision/latest/scale-to-width-down/120?cb=20210809081331",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d0/Card_1018110_thumb.png/revision/latest/scale-to-width-down/120?cb=20200202233829"
]

cualquier_sr_goku2 = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/40/Card_1001720_thumb.png/revision/latest/scale-to-width-down/120?cb=20150914221625",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/65/Card_1003750_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026231128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/62/Card_1001990_thumb.png/revision/latest/scale-to-width-down/120?cb=20151009162655",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9a/Card_1001120_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925131432",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

class Multigoku(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multigoku online")

  #Comandos del bot
  @commands.command()
  async def multigoku(self, ctx):
    await ctx.send("**Empezando multisummon:**")
    await ctx.send("<:SSR_eclair:971672682712141844> Cell <:INT_icon:971673169943466024> (<:LR_logo_apng:978185948787531816>) - 5 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
    await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
    await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
    await ctx.send( random.choice(animaciones_summons))
    puntos = 0
    if random.randint(1, 10000) >= 9500:
      random1 = random.choice(featured_ssr_goku2)
      await ctx.send(random1)
      if random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/20/Card_1017880_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035025":
        puntos = puntos + 5
      else:
        puntos = puntos + 3
    else:
      await ctx.send(
                "<:SSR_eclair:971672682712141844> Random")
      puntos = puntos + 2
      for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_goku2)
                await ctx.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/20/Card_1017880_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035025":
                    puntos = puntos + 5
                else:
                    puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_goku2))
                puntos = puntos + 1
            else:
                await ctx.send(
                    "<:R_eclair:971673105024045056> Personaje kk")
      await ctx.send(f"Total de puntos: {puntos}")
      if puntos >= 15:
          await ctx.send("https://i.pinimg.com/564x/4c/4d/88/4c4d8867c58389c11d6d05221aa16632.jpg")
      elif puntos >= 10:
          await ctx.send("https://i.pinimg.com/550x/09/19/b6/0919b6dcf57e6a6b4bf31ac5fd1e7928.jpg")
      elif puntos >= 7:
          await ctx.send("https://i.ytimg.com/vi/ffHN6_8HDuI/mqdefault.jpg")
      elif puntos >= 5:
          await ctx.send("https://i.pinimg.com/736x/35/b7/3e/35b73e01e63b253e041e874aa590681e.jpg")
      else: 
          await ctx.send("https://pbs.twimg.com/media/EaLXbstWAAETAaT.jpg")
      await ctx.send("**Multisummon finalizado**")


def setup(client):
	client.add_cog(Multigoku(client))