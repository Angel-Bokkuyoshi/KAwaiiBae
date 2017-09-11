import discord
import resources as res
import random

class Entertainment:

    def __init__(self, my_bot):
        self.__settings = res.Settings()
        self.__settings.name = "Entertainment"
        self.__settings.descs = {"blob":"Bliss or Burn! which will it be?: //blob your mom", "react":"Reacts to message with your content in emojis."}
        self.__settings.open_ = True
        self.lis = {my_bot.pref + "blob":self.BloB, my_bot.pref + "react":self.react}

    def settings(self):
        return self.__settings

    async def BloB(self, message, msg, my_bot):
        async def burn(mention):
            url = random.choice(res.burn)
            em = discord.Embed()
            em.set_image(url = url)
            await my_bot.bot.send_message(message.channel, (mention + ": Burn!").join(res.emb))
            await my_bot.bot.send_message(message.channel, embed = em)

        async def bliss(mention):
            url = random.choice(res.bliss)
            em = discord.Embed()
            em.set_image(url = url)
            await my_bot.bot.send_message(message.channel, (mention + ": Ah... bliss").join(res.emb))
            await my_bot.bot.send_message(message.channel, embed = em)

        mention = msg.split(None, 1)[1]
        choices = [burn, bliss]
        choice = random.choice(choices)
        await choice(mention)

    async def react(self, message, msg, my_bot):
        param1 = msg.split(None,1)[1].lower()
        param1 = list(param1)
        for i in param1:
            try:
                await my_bot.bot.add_reaction(message, res.alphanum[i])
            except: pass

    def open(self):
        return self.__settings.open_
        
