import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_buu = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/6b/Card_1001960_thumb.png/revision/latest/scale-to-width-down/120?cb=20151022175148",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b4/Card_1020520_thumb.png/revision/latest/scale-to-width-down/120?cb=20200829051523",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/aa/Card_1008140_thumb.png/revision/latest/scale-to-width-down/120?cb=20160901130901",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/cf/Card_1001970_thumb.png/revision/latest/scale-to-width-down/120?cb=20151022214945",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/4b/Card_1001950_thumb.png/revision/latest/scale-to-width-down/120?cb=20180901002337",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/72/Card_1018670_thumb.png/revision/latest/scale-to-width-down/120?cb=20200507075541",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d7/Card_1013180_thumb.png/revision/latest/scale-to-width-down/120?cb=20180708215012",
]

cualquier_sr_buu = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/bd/Card_1003550_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925221457",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1010590_thumb.png/revision/latest/scale-to-width-down/120?cb=20170925121648",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/fa/Card_1004560_thumb.png/revision/latest/scale-to-width-down/120?cb=20160403133232",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/d7/Card_1003820_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026231413",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/90/Card_1001980_thumb.png/revision/latest/scale-to-width-down/120?cb=20151022215410",
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

class Multibuu(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multibuu online")

  #Comandos del bot
  @commands.command()
  async def multibuu(self, ctx):
        await ctx.send("**Empezando multisummon:**")
        await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
        await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
        await ctx.send("<:SR_eclair:971673046496731166> - 1 punto")
        await ctx.send(
            random.choice(animaciones_summons))
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_buu)
            await ctx.send(random1)
            puntos = puntos + 3
        else:
            await ctx.send(
                "<:SSR_eclair:971672682712141844> Random")
            puntos = puntos + 2
        for i in range(0, 9):
            numero = random.randint(1, 10000)
            if numero >= 9500:
                random2 = random.choice(featured_ssr_buu)
                await ctx.send(random2)
                puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_buu))
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
	client.add_cog(Multibuu(client))