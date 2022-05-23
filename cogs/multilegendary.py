import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_legendary = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/91/Card_1024330_thumb.png/revision/latest/scale-to-width-down/120?cb=20220512065240",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/64/Card_1021120_thumb.png/revision/latest/scale-to-width-down/120?cb=20201214024421",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b1/Card_1010050_thumb.png/revision/latest/scale-to-width-down/120?cb=20170707192320",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/0e/Card_1001700_thumb.png/revision/latest/scale-to-width-down/120?cb=20150901181624",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/69/Card_1022690_thumb.png/revision/latest/scale-to-width-down/120?cb=20211230082907",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c0/Card_1001690_thumb.png/revision/latest/scale-to-width-down/120?cb=20150901101545",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/40/Card_1017560_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035021",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/e/ee/Card_1023370_thumb.png/revision/latest/scale-to-width-down/120?cb=20220127091212",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/d/dc/Card_1010110_thumb.png/revision/latest/scale-to-width-down/120?cb=20170707201613"
]

cualquier_sr_legendary = [
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/90/Card_1001000_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925123210",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/99/Card_1000230_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925114128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/65/Card_1003750_thumb.png/revision/latest/scale-to-width-down/120?cb=20151026231128",
    "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/5c/Card_1001710_thumb.png/revision/latest/scale-to-width-down/120?cb=20150908101027",
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
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random",
    "<:SR_eclair:971673046496731166> Random"
]

class Multilegendary(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multilegendary online")

  #Comandos del bot
  @commands.command()
  async def multilegendary(self, ctx):
        await ctx.send("**Empezando multisummon:**")
        await ctx.send("<:LR_logo_apng:978185948787531816> featured - 5 puntos")
        await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
        await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
        await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
        await ctx.send(
            random.choice(animaciones_summons))
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_legendary)
            await ctx.send(random1)
            if random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/91/Card_1024330_thumb.png/revision/latest/scale-to-width-down/120?cb=20220512065240":
              puntos = puntos + 5
            elif random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/64/Card_1021120_thumb.png/revision/latest/scale-to-width-down/120?cb=20201214024421":
              puntos = puntos + 5
            elif random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b1/Card_1010050_thumb.png/revision/latest/scale-to-width-down/120?cb=20170707192320":
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
                random2 = random.choice(featured_ssr_legendary)
                await ctx.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/91/Card_1024330_thumb.png/revision/latest/scale-to-width-down/120?cb=20220512065240":
                  puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/64/Card_1021120_thumb.png/revision/latest/scale-to-width-down/120?cb=20201214024421":
                  puntos = puntos + 5
                elif random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/b1/Card_1010050_thumb.png/revision/latest/scale-to-width-down/120?cb=20170707192320":
                  puntos = puntos + 5
                else:
                  puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_legendary))
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
	client.add_cog(Multilegendary(client))