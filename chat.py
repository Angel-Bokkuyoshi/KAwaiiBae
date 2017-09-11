import discord
import asyncio
import resources as res

class Chat:

    def __init__(self, my_bot):
        self.__settings = res.Settings()
        self.__settings.name = "SmoothChat"
        self.__settings.descs = {"chat on":"Activates the shifting chat that sends new messages above ``preposts`` amount of post.", "chat off":"Deactivates the shifting chat.",
                                "chat preposts":"Sets the ``preposts`` value."}
        self.__settings.open_ = True
        self.postignore = 0
        self.chat_on
        self.lis = {my_bot.pref + "chat on":self.chat_on, my_bot.pref + "chat off":self.chat_off, my_bot.pref + "chat preposts":self.chat_preposts}

    def settings(self):
        return self.__settings

    async def chat_on(self, message, msg, my_bot):
        @res.manage_messages(message, msg, my_bot)
        async def run():
            m_message = await my_bot.bot.send_message(message.channel, "Chat Startpoint".join(res.emb))
            channel = message.channel
            self.chat_on = True
            while self.chat_on:
                tmp = await my_bot.bot.wait_for_message(channel = channel)
                if self.postignore == 0:
                    await my_bot.bot.delete_message(tmp)
                    tmp2 = m_message.content
                    if len(tmp2) + len(tmp.content) <= 440:
                        tmp2 += "\n" + tmp.author.name + ": " + tmp.content
                    else:
                        tmp2 = tmp.author.name + ": " + tmp.content
                    m_message = await my_bot.bot.edit_message(m_message, tmp2)

                if self.postignore > 0:
                    self.postignore -= 1
            await my_bot.bot.send_message(message.channel, "Chat Endpoint".join(res.emb))
                
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)

    async def chat_off(self, message, msg, my_bot):
        @res.manage_messages(message, msg, my_bot)
        async def run():
            self.chat_on = False
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)

    async def chat_preposts(self, message, msg, my_bot):
        val = msg.split()[2]
        try:
            self.postignore = int(val)
            await my_bot.bot.add_reaction(message, res.white_tick)
        except:
            await my_bot.bot.add_reaction(message, res.anger)
        
    def open(self):
        return (self.__settings.open_)

