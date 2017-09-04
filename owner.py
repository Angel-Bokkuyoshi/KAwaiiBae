import discord
import resources as res

class Owner:

    def __init__(self, my_bot):
        self.__settings = res.Settings()
        self.__settings.name = "Owner"
        self.__settings.descs = {"announce":"None of your business m8.", "serverlist":"Big nose you got there.", "channel default":"Sets the channel for announcements: //channel default <id>"}
        self.__settings.open_ = True
        self.lis = {my_bot.pref + "announce":self.announce, my_bot.pref + "serverlist":self.serverlist, my_bot.pref + "channel default":self.channel_default}

    def settings(self):
        return self.__settings

    async def announce(self, message, msg, my_bot):
        @res.owner(message, msg, my_bot)
        async def run():
            em = discord.Embed(color = discord.Color.orange())
            em.set_author(name = my_bot.owner.name, icon_url = my_bot.owner.avatar_url)
            em.add_field(name = "Announcement", value = msg.split(None, 1)[1], inline = True)
            for a in my_bot.servers:
                try:
                    await my_bot.bot.send_message(my_bot.servers[a].default_channel,embed = em)
                except: pass
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)

    async def serverlist(self, message, msg, my_bot):
        @res.owner(message, msg, my_bot)
        async def run():
            em = discord.Embed(title = "=========SERVERS========", description = "All servers the bot is currently in", color = discord.Color.purple(), type = "rich")
            em.set_author(icon_url = my_bot.bot.user.avatar_url, name = my_bot.bot.user.name)
            reply = ""
            for a in my_bot.servers:
                reply += my_bot.servers[a].server.name + "\n"
            em.add_field(name = "List", value = reply, inline = False)   
            await my_bot.bot.send_message(message.channel, embed = em)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
            
    async def channel_default(self, message, msg, my_bot):
        @res.manage_channels(message, msg, my_bot)
        async def run():
            lis = msg.split()
            channel = my_bot.bot.get_channel(lis[2])
            my_bot.servers[message.server.id].default_channel = channel
            await my_bot.bot.add_reaction(message, res.white_tick)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except:
            await my_bot.bot.add_reaction(message, res.anger)
        
    def open(self):
        return (self.__settings.open_)
