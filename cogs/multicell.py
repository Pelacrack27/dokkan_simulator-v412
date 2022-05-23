import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_cell = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/11/Card_1024370_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426051407",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/1/1c/Card_1024240_thumb.png/revision/latest/scale-to-width-down/120?cb=20220426063352",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1017610_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035023",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/28/Card_1022820_thumb.png/revision/latest/scale-to-width-down/120?cb=20211202073154",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/89/Card_1021280_thumb.png/revision/latest/scale-to-width-down/120?cb=20210331131353",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/2/24/Card_1019620_thumb.png/revision/latest/scale-to-width-down/120?cb=20201106101145",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/35/Card_1020080_thumb.png/revision/latest/scale-to-width-down/120?cb=20201004105257",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8a/Card_1018260_thumb.png/revision/latest/scale-to-width-down/120?cb=20200402002017"
]

cualquier_sr_cell = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4f/Card_1000080_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922211527",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/52/Card_1002790_thumb.png/revision/latest/scale-to-width-down/120?cb=20171123185807",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b9/Card_1003250_thumb.png/revision/latest/scale-to-width-down/120?cb=20151015213043",
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

class Multicell(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multicell online")

  #Comandos del bot
  @commands.command()
  async def multicell(self, ctx):
        await ctx.send("**Empezando multisummon:**")
        await ctx.send("<:SSR_eclair:971672682712141844> Gohan SSJ <:AGL_icon:971673135122350161> (<:LR_logo_apng:978185948787531816>) - 5 puntos")
        await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
        await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
        await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
        await ctx.send(
            random.choice(animaciones_summons))
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_cell)
            await ctx.send(random1)
            if random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1017610_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035023":
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
                random2 = random.choice(featured_ssr_cell)
                await ctx.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/8/8b/Card_1017610_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035023":
                    puntos = puntos + 5
                else:
                    puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_cell))
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
	client.add_cog(Multicell(client))