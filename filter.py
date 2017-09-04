import discord
import resources as res
import re
import asyncio

async def filter_(server, my_bot):
    while server.filter_on:
        if len(server.msg_stack) > 1:
            tmp = server.msg_stack[len(server.msg_stack)-1]
            for a in server.filter_targets:
                if re.match(re.compile(a), tmp.content) or a.upper() in tmp.content.upper():
                    await my_bot.bot.delete_message(tmp)
            server.msg_stack.remove(tmp)
        await asyncio.sleep(0.2)

class Filter:
    
    def __init__(self, my_bot):
        self.__settings = res.Settings()
        self.__settings.name = "Filter"
        self.__settings.descs = {"filter toggle":"Turns the filter on or off.", "filter add":"Adds a target to the target list", "filter del":"Removes a target from the target list",
                                 "filter regadd":"Adds a python regular expression to the target list. LEarn how to use regexes at https://docs.python.org/2/howto/regex.html"}
        self.__settings.open_ = True
        self.lis = {my_bot.pref + "filter toggle":self.toggle_filter, my_bot.pref + "filter add":self.filter_add, my_bot.pref + "filter del":self.filter_del,
                    my_bot.pref + "filter regadd":self.filter_add_regex}
        
    def settings(self):
        return self.__settings

    async def toggle_filter(self, message, msg, my_bot):
        @res.manage_messages(message, msg, my_bot)
        async def run():
            a = my_bot.servers[message.server.id]
            a.filter_on = not a.filter_on
            await a.update()
            await my_bot.bot.add_reaction(message, res.white_tick)
            if a.filter_on:
                await filter_(a, my_bot)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except:
            await my_bot.bot.add_reaction(message, res.anger)

    async def filter_add(self, message, msg, my_bot):
        @res.manage_messages(message, msg, my_bot)
        async def run():
            server = my_bot.servers[message.server.id]
            lis = msg.split(None, 2)
            server.filter_targets.append(lis[2])
            await server.update()
            await my_bot.bot.add_reaction(message, res.white_tick)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except:
            await my_bot.bot.add_reaction(message, res.anger)

    async def filter_add_regex(self, message, msg, my_bot):
        @res.manage_messages(message, msg, my_bot)
        async def run():
            server = my_bot.servers[message.server.id]
            val = msg.split()[2]
            raw = ""
            server.filter_targets.append(val)
            await server.update()
            await my_bot.bot.add_reaction(message, res.white_tick)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except:
            await my_bot.bot.add_reaction(message, res.anger) 

    async def filter_del(self, message, msg, my_bot):
        @res.manage_messages(message, msg, my_bot)
        async def run():
            server = my_bot.servers[message.server.id]
            lis = msg.split(None, 2)
            server.filter_targets.remove(lis[2])
            await server.update()
            await my_bot.bot.add_reaction(message, res.white_tick)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except:
            await my_bot.bot.add_reaction(message, res.anger)

    def open(self):
        return (self.__settings.open_)

