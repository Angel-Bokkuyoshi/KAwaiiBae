import os
import datetime
import json

try:
    import discord
except ImportError:
    print("Failure to import discord.py, please install the discord.py API")
    exit(1)
    
from discord.ext.commands import Bot
import logging

try:
    import resources as res
    from roles import Roles
    from utility import Utility
    from owner import Owner
    from filter import Filter
    from chat import Chat
    from entertainment import Entertainment
except ImportError:
    print("One or more modules are missing, this bot cannot work without them.")
    exit(1)

logging.basicConfig(level=logging.INFO) #Activate Logging
storage = "storage/"
class Role(discord.Role):
    def __init__(self, role):
        self.role = role
        self.raving = False

class Server():
    def __init__(self, server):
        self.server = server
        self.default_channel = server.default_channel
        roles = list(map(lambda a: Role(a), server.roles))
        self.roles = {}
        for a in roles:
            self.roles[a.role.name] = a
        self.filter_targets = list() #Storage for regex strings
        self.filter_on = False
        self.log_og = False
        self.log_channel = "" #Storage for the Log channel name
        self.log_types = list() #Storage for Log type strings
        self.welcome_on = False
        self.welcome_channel = "" #Storage for the Welcome channel name
        self.welcome = "" #Storage for the welcome message
        self.farewell_on = False
        self.farewell_channel = "" #Storage for the Farewell channel name
        self.farewell = "" #Storage for the farewell message
        self.msg_stack = list() #Recieved messages

    async def update(a):
        file = open(storage + a.server.id + ".json", "w")
        aa = {"filter_targets":a.filter_targets, "log_channel":a.log_channel, "log_types":a.log_types, "welcome_on":a.welcome_on, "welcome_channel":a.welcome_channel, "welcome":a.welcome,
              "farewell_on":a.farewell_on, "farewell_channel":a.farewell_channel, "farewell":a.farewell}
        json.dump(aa, file)

class Command: #Class used to extend functionality of commands
    def __init__(self, name, function):
        self.name = name
        self.apply = function

class KBot: #CORE BOT

    def __init__(self):
        self.modules = list() #Command Modules
        self.cmds = {} #Commands
        self.cmdescs = {} #command Descriptions
        self.bot = Bot(None)
        self.pref = "//"
        self.link = "https://discordapp.com/oauth2/authorize?client_id=354353934074380298&scope=bot&permissions=271674432"
        self.owner = None #Owner Info
        self.servers = {}
        
        #Adding Commands
        if Owner(self).open():
            self.modules.append(Owner(self))
            self.cmdescs.update(Owner(self).settings().descs)
            for a in Owner(self).lis:
                self.cmds[a] = Command(a, self.modules[0].lis[a])
        if Roles(self).open():
            self.modules.append(Roles(self))
            self.cmdescs.update(Roles(self).settings().descs)
            for a in Roles(self).lis:
                self.cmds[a] = Command(a, self.modules[1].lis[a])
        if Filter(self).open():
            self.modules.append(Filter(self))
            self.cmdescs.update(Filter(self).settings().descs)
            for a in Filter(self).lis:
                self.cmds[a] = Command(a, self.modules[2].lis[a])
        if Utility(self).open():
            self.modules.append(Utility(self))
            self.cmdescs.update(Utility(self).settings().descs)
            for a in Utility(self).lis:
                self.cmds[a] = Command(a, self.modules[3].lis[a])
        if Chat(self).open():
            self.modules.append(Chat(self))
            self.cmdescs.update(Chat(self).settings().descs)
            for a in Chat(self).lis:
                self.cmds[a] = Command(a, self.modules[4].lis[a])
        if Entertainment(self).open():
            self.modules.append(Entertainment(self))
            self.cmdescs.update(Entertainment(self).settings().descs)
            for a in Entertainment(self).lis:
                self.cmds[a] = Command(a, self.modules[5].lis[a])
            
    def start(self, token): #Starts Bot
        self.bot.run(token)
        
my_bot = KBot()

@my_bot.bot.event
async def on_ready():
    appinfo = await my_bot.bot.application_info()
    my_bot.owner = appinfo.owner
    await my_bot.bot.change_presence(game = discord.Game(name = "type " + my_bot.pref + "help")) #Sets Playing status
    servers = list(map(lambda x: Server(x), my_bot.bot.servers)) #Collects all the servers the bot is in
    for a in servers:
        my_bot.servers[a.server.id] = a

    for a in my_bot.servers: #Makes a json file for new servers
        try:
            file = open(storage + my_bot.servers[a].server.id + ".json")
            aa = json.load(file)
            my_bot.servers[a].filter_targets = aa["filter_targets"]
            my_bot.servers[a].log_channel = aa["log_channel"]
            my_bot.servers[a].log_types = aa["log_types"]
            my_bot.servers[a].welcome_on = aa["welcome_on"]
            my_bot.servers[a].welcome_channel = aa["welcome_channel"]
            my_bot.servers[a].welcome = aa["welcome"]
            my_bot.servers[a].farewell_on = aa["farewell_on"]
            my_bot.servers[a].welcome_channel = aa["farewell_channel"]
            my_bot.servers[a].welcome = aa["farewell"]
        except IOError:
            print("No json file for server, creating one.")
            file = open(storage + my_bot.servers[a].server.id + ".json", "w")
            aa = {"filter_targets":my_bot.servers[a].filter_targets, "log_channel":my_bot.servers[a].log_channel, "log_types":my_bot.servers[a].log_types, "welcome_on":my_bot.servers[a].welcome_on,
                  "welcome_channel":my_bot.servers[a].welcome_channel, "welcome":my_bot.servers[a].welcome, "farewell_on":my_bot.servers[a].farewell_on,
                  "farewell_channel":my_bot.servers[a].farewell_channel, "farewell":my_bot.servers[a].farewell}
            json.dump(aa, file)
@my_bot.bot.event
async def on_server_join(server):
    my_bot.servers[server.id] = Server(server)
    a = my_bot.servers[server.id]
    print("No json file for server, creating one.")
    file = open(storage + a.server.id + ".json", "w")
    aa = {"filter_targets":a.filter_targets, "log_channel":a.log_channel, "log_types":a.log_types, "welcome_on":a.welcome_on, "welcome_channel":a.welcome_channel, "welcome":a.welcome, "farewell_on":a.farewell_on, "farewell_channel":a.farewell_channel, "farewell":a.farewell}
    json.dump(aa, file)
    await my_bot.bot.send_message(server.default_channel, "Thank you for using KawaiiBae! If you do not want this channel to be used for Announcements\nSet your default channel with //channel default channelID")
    
@my_bot.bot.event
async def on_server_role_create(role):
    my_bot.servers[role.server.id].roles[role.name] = Role(role)

@my_bot.bot.event
async def on_server_role_update(before, after):
    if after.name != before.name:
        del my_bot.servers[before.server.id].roles[before.name]
        my_bot.servers[after.server.id].roles[after.name] = Role(after)

@my_bot.bot.event
async def on_server_role_delete(role):
    del my_bot.servers[role.server.id].roles[role.name]

@my_bot.bot.event
async def on_message(message):    
    print(message.server.name + "  " + message.channel.name)
    server = my_bot.servers[message.server.id]
    server.msg_stack.append(message)
    msg = message.content
    render = list()
    try:
        render.append(msg.split()[0] + msg.split()[1] + msg.split()[2])
    except: pass
    try:
        render.append(msg.split()[0]+ msg.split()[1])
    except: pass
    try:
        render.append(msg.split()[0])
    except: pass
    
    for i in render:   
        try:
            await my_bot.cmds[i].apply(message, msg, my_bot)
        except KeyError or TypeError:
            pass
    
file = open(storage + "config.json")
aa = json.load(file)              
my_bot.start(aa["id"]) #Run bot
