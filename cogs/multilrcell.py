import discord
import random
from discord.ext import commands

animaciones_summons = [
  "https://c.tenor.com/N3ley5BmlZwAAAAM/dokkan-battle-vegito.gif",
  "https://c.tenor.com/E30Z_TKyvn4AAAAM/dokkan-summon.gif",
  "https://c.tenor.com/c_MZLKFOgV0AAAAM/summon-anniversary.gif"
]

featured_ssr_lrcell = [
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1014920_thumb.png/revision/latest/scale-to-width-down/120?cb=20181017101240",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/c/c0/Card_1001690_thumb.png/revision/latest/scale-to-width-down/120?cb=20150901101545",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/40/Card_1017560_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035021",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/61/Card_1017580_thumb.png/revision/latest/scale-to-width-down/120?cb=20190829035022",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/0/05/Card_1003790_thumb.png/revision/latest/scale-to-width-down/120?cb=20151030230959",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a5/Card_1003780_thumb.png/revision/latest/scale-to-width-down/120?cb=20151030230620",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/a/a5/Card_1003780_thumb.png/revision/latest/scale-to-width-down/120?cb=20151030230620",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/92/Card_1007860_thumb.png/revision/latest/scale-to-width-down/120?cb=20190316091032"
]

cualquier_sr_lrcell = [
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/75/Card_1002140_thumb.png/revision/latest/scale-to-width-down/120?cb=20151009204458",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/f/f7/Card_1000860_thumb.png/revision/latest/scale-to-width-down/120?cb=20180902213728",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/b/be/Card_1000040_thumb.png/revision/latest/scale-to-width-down/120?cb=20150922210156",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/4/40/Card_1001720_thumb.png/revision/latest/scale-to-width-down/120?cb=20150914221625",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/3/3b/Card_1001010_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925123755",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/5/58/Card_1000240_thumb.png/revision/latest/scale-to-width-down/120?cb=20150908133942",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/6/68/Card_1010520_thumb.png/revision/latest/scale-to-width-down/120?cb=20170915100349",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/77/Card_1000990_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925122917",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/7/71/Card_1000220_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925113850",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/90/Card_1001000_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925123210",
  "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/99/Card_1000230_thumb.png/revision/latest/scale-to-width-down/120?cb=20150925114128",
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


class Multilrcell(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Eventos del bot
  @commands.Cog.listener()
  async def on_ready(self):
    print("multilrcell online")

  #Comandos del bot
  @commands.command()
  async def multilrcell(self, ctx):
        await ctx.send("**Empezando multisummon:**")
        await ctx.send("<:SSR_eclair:971672682712141844> Cell <:PHY_icon:971673203267231744> (<:LR_logo_apng:978185948787531816>) - 5 puntos")
        await ctx.send("<:SSR_eclair:971672682712141844> Featured - 3 puntos")
        await ctx.send("<:SSR_eclair:971672682712141844> No featured - 2 puntos")
        await ctx.send("<:SR_eclair:971673046496731166>  - 1 punto")
        await ctx.send(
            random.choice(animaciones_summons))
        puntos = 0
        if random.randint(1, 10000) >= 9500:
            random1 = random.choice(featured_ssr_lrcell)
            await ctx.send(random1)
            if random1 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1014920_thumb.png/revision/latest/scale-to-width-down/120?cb=20181017101240":
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
                random2 = random.choice(featured_ssr_lrcell)
                await ctx.send(random2)
                if random2 == "https://static.wikia.nocookie.net/dbz-dokkanbattle/images/9/9c/Card_1014920_thumb.png/revision/latest/scale-to-width-down/120?cb=20181017101240":
                  puntos = puntos + 5
                else:
                  puntos = puntos + 3
            elif numero >= 9000:
                await ctx.send(
                    "<:SSR_eclair:971672682712141844> Random")
                puntos = puntos + 2
            elif numero >= 3000:
                await ctx.send(random.choice(cualquier_sr_lrcell))
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
	client.add_cog(Multilrcell(client))