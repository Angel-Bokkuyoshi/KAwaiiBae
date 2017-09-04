import discord
import resources as res
import datetime


class Utility:

    def __init__(self, my_bot):
        self.__settings = res.Settings()
        self.__settings.name = "Utility"
        self.__settings.descs = {"time":"Tells you the time given a time zone(GMT) or not(UTC).", "calc":"Math SON!", "invite":"Generates an invite link", "help":"Basic info and list of commands",
                                 "commands":"Tells you what a command does.", "formula set":"Sets a mathematical formula.", "formula show":"Shows the formula",
                                 "formula map":"Maps the variables in the order (x,y,z)"}
        self.__settings.open_ = True
        self.lis = {my_bot.pref + "time":self.time, my_bot.pref + "calc":self.calculate, my_bot.pref + "invite":self.invite, my_bot.pref + "help":self.help, my_bot.pref + "commands":self.commands,
                    my_bot.pref + "formula set":self.set_formula, my_bot.pref + "formula show":self.show_formula, my_bot.pref + "formula map":self.map}
        self.formula = ""

    def settings(self):
        return self.__settings

    async def time(self, message, msg, my_bot):
        lis = msg.split()
        minutes = 0
        try:
            assert len(lis)>1
            lis = lis[1].split(":")
            assert int(lis[0]) >= -12 and int(lis[0]) <= 12
            if len(lis) > 1:
                assert int(lis[1]) == 0 or int(lis[1]) == 30
                minutes = int(lis[1])
            me = datetime.timezone(datetime.timedelta(hours = int(lis[0]), minutes = minutes))
            await my_bot.bot.send_message(message.channel, "{0} the time is ``{1}``".format(message.author.mention, str(datetime.datetime.now(me))[11:16] + ' @GMT ' + ":". join(lis)))
        except AssertionError:
            await my_bot.bot.send_message(message.channel, "No recognized time zone Given {0} the time is {1}".format(message.author.mention, str(datetime.datetime.now())[11:16]))
            
    async def set_formula(self, message, msg, my_bot):
        lis = msg.split()[2]
        if lis.isalnum:
            self.formula = lis
            await my_bot.bot.add_reaction(message, res.white_tick)
        else:
            await my_bot.bot.add_reaction(message, res.anger)

    async def show_formula(self, message, msg, my_bot):
        await my_bot.bot.send_message(message.channel, self.formula.join(res.emb2))

    async def map(self, message, msg, my_bot):
        lis = msg.split()
        try: 
            x = lis[2]
            y = lis[3]
            z = lis[4]
        except: pass

        expr = ""
        formula = list(self.formula)
        
        if "x" in formula:
            for i in range(0, len(formula)):
                formula[i] = x if formula[i] == "x" else formula[i]
        if "y" in formula:
            for i in range(0, len(formula)):
                formula[i] = y if formula[i] == "y" else formula[i]
        if "z" in formula:
            for i in range(0, len(formula)):
                formula[i] = z if formula[i] == "z" else formula[i]

        for a in formula:
            expr += a
                
        try:
            await my_bot.bot.send_message(message.channel, str(res.calculate(expr)).join(res.emb))
        except ZeroDivisionError:
            await my_bot.bot.add_reaction(message, res.anger)
        except ValueError:
            await my_bot.bot.add_reaction(message, res.anger)

    async def calculate(self, message, msg, my_bot):
        lis = msg.split()[1]
        try:
            await my_bot.bot.send_message(message.channel, str(res.calculate(lis)).join(res.emb))
        except ZeroDivisionError:
            await my_bot.bot.add_reaction(message, res.anger)
        except ValueError:
            await my_bot.bot.add_reaction(message, res.anger)

    async def invite(self, message, msg, my_bot):
        await my_bot.bot.send_message(message.channel, my_bot.link)

    async def help(self, message, msg, my_bot):
        em = discord.Embed(title = "Help Moe" + res.heart,
        description = "The List of all Command objects, use //commands <cmd> for details. The bot is currently hosted on a free Heroku Server and so can only store any data for 24 hours.\n"
                    + "The bot requires hierarchy and permissions to do some commands. The bot will respond to your messages for some commands, a green tick is always good. Bad input/Bot is Forbidden(:anger:). User is Forbidden(:no_entry_sign:).",
        type = "rich", color = discord.Color.purple())
        em.set_author(name = my_bot.bot.user.name, icon_url = my_bot.bot.user.avatar_url)
        for a in my_bot.modules:
            reply = ""
            for i in a.lis:
                reply += "\n" + i[2:].join(res.emb)
            reply += "\n\n"
            em.add_field(name = a.settings().name, value = reply, inline = True)
        
        await my_bot.bot.send_message(message.channel, embed = em)

    async def commands(self, message, msg, my_bot):
        try:
            query = msg.split(None, 1)[1]
        except IndexError:
            await my_bot.bot.add_reaction(message, res.anger)
        em = discord.Embed(color = discord.Color.orange())
        em.set_author(name = my_bot.owner.name, icon_url = my_bot.owner.avatar_url)
        em.add_field(name = query, value = my_bot.cmdescs[query], inline = True)
        await my_bot.bot.send_message(message.channel, embed = em)

    def open(self):
        return (self.__settings.open_)
