import discord
import random
import resources as res
import asyncio

class Roles:

    def __init__(self, my_bot):
        self.__settings = res.Settings()
        self.__settings.name = "Roles"
        self.__settings.descs = {"rave on":"Turns on flashing role colors for a given role://rave on \"some role\" red dark_blue\nColors: red,green,blue,white,orange,teal,gold,magenta,purple and dark versions",
                                 "rave off":"Turns off flashing role colors for a given role and returns it to default.", "role color":"Set the color of a role given a hex value: //role color ROLE a1acbb"}
        self.__settings.open_ = True
        self.lis = {my_bot.pref + "rave on":self.rave, my_bot.pref + "rave off":self.rave_off, my_bot.pref + "role color":self.role_color}

    def settings(self):
        return self.__settings
    
    async def rave(self, message, msg, my_bot):
        @res.administrator(message, msg, my_bot)
        async def run():
            lis = msg.split("\"",2)
            if lis[0] != msg:
                lis2 = lis[0].split()
                lis2.append(lis[1])
                lis2 += lis[2].split()
            else:
                lis2 = msg.split()   
            if len(lis2) >= 5:
                pass
            else:
                await my_bot.bot.add_reaction(message, res.anger)
                return
            role = lis2[2]
            count = 0
            ravecolors = lis2[3:]
            role = my_bot.servers[message.server.id].roles[role]
            role.raving = True
            while role.raving:
                if ravecolors[count % len(ravecolors)].lower() == "red":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.red())
                elif ravecolors[count % len(ravecolors)].lower() == "blue":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.blue())
                elif ravecolors[count % len(ravecolors)].lower() == "green":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.green())
                elif ravecolors[count % len(ravecolors)].lower() == "white":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.lighter_grey())
                elif ravecolors[count % len(ravecolors)].lower() == "blue":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.blue())
                elif ravecolors[count % len(ravecolors)].lower() == "orange":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.orange())
                elif ravecolors[count % len(ravecolors)].lower() == "teal":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.teal())
                elif ravecolors[count % len(ravecolors)].lower() == "gold":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.gold())
                elif ravecolors[count % len(ravecolors)].lower() == "purple":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.purple())
                elif ravecolors[count % len(ravecolors)].lower() == "magenta":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.magenta())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_red":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_red())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_blue":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_blue())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_green":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_green())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_white":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_default())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_blue":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_blue())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_orange":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_orange())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_teal":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_teal())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_gold":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_gold())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_purple":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_purple())
                elif ravecolors[count % len(ravecolors)].lower() == "dark_magenta":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.dark_magenta())
                elif ravecolors[count % len(ravecolors)].lower() == "default":
                    await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.default())
                else:
                    await my_bot.bot.add_reaction(message, res.anger)
                    break
                count += 1
                await asyncio.sleep(0.5)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except discord.errors.Forbidden:
            await my_bot.bot.add_reaction(message, res.anger)
        except:
            await my_bot.bot.add_reaction(message, res.anger)

    async def rave_off(self, message, msg, my_bot):
        @res.administrator(message, msg, my_bot)
        async def run():
            lis = msg.split(None, 2)
            if "\"" in lis[2]:
                role = lis[2].split("\"")[1]
            else:
                role = lis[2]
            role = my_bot.servers[message.server.id].roles[role]
            role.raving = False
            await my_bot.bot.edit_role(message.server, role.role, color = discord.Color.default())
            await my_bot.bot.add_reaction(message, res.white_tick)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except discord.errors.Forbidden:
            await my_bot.bot.add_reaction(message, res.anger)
        except:
            await my_bot.bot.add_reaction(message, res.anger)

    async def role_color(self, message, msg, my_bot):
        @res.administrator(message, msg, my_bot)
        async def run():
            lis = msg.split("\"",2)
            if lis[0] != msg:
                lis2 = lis[0].split()
                lis2.append(lis[1])
                lis2.append(lis[2])
            else:
                lis2 = msg.split()
            role = lis2[2]
            colorhex = int(lis2[3], 16)
            color = discord.Color(colorhex)
            role = my_bot.servers[message.server.id].roles[role]
            role.raving = False
            await my_bot.bot.edit_role(message.server, role.role, color = color)
            await my_bot.bot.add_reaction(message, res.white_tick)
        try:
            await run()
        except AssertionError:
            await my_bot.bot.add_reaction(message, res.no_access)
        except discord.errors.Forbidden:
            await my_bot.bot.add_reaction(message, res.anger)
        #except:
            #await my_bot.bot.add_reaction(message, res.anger)
    
    def open(self):
        return (self.__settings.open_)

