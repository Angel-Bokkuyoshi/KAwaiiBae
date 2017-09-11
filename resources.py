#All resources needed for Kb's functionality
from enum import Enum

#Global
class Settings:
    name = None
    descs = None
    open_ = None

def manage_messages(message, msg, my_bot):
    def wrapper(func):
        async def returns():
            if not message.author.permissions_in(message.channel).manage_messages:
                raise AssertionError
            else:
                await func()
        return returns
    return wrapper

def administrator(message, msg, my_bot):
    def wrapper(func):
        async def returns():
            if not message.author.server_permissions.administrator:
                raise AssertionError
            else:
                await func()
        return returns
    return wrapper
    

def manage_channels(message, msg, my_bot):
    def wrapper(func):
        async def returns():
            if not message.author.server_permissions.manage_channels:
                raise AssertionError
            else:
                await func()
        return returns
    return wrapper

def owner(message, msg, my_bot):
    def wrapper(func):
        async def returns():
            if not message.author == my_bot.owner:
                raise AssertionError
            else:
                await func()
        return returns
    return wrapper

emb = ["``", "``"]
emb2 = ["```", "```"]
bold = ["**", "**"]

heart = "\u2764"
anger = "\U0001F4A2"
white_tick = "\u2705"
no_access = "\U0001F6AB"
alphanum = {"0":"0\N{COMBINING ENCLOSING KEYCAP}", "1":"1\N{COMBINING ENCLOSING KEYCAP}", "2":"2\N{COMBINING ENCLOSING KEYCAP}", "3":"3\N{COMBINING ENCLOSING KEYCAP}", "4":"4\N{COMBINING ENCLOSING KEYCAP}",
            "5":"5\N{COMBINING ENCLOSING KEYCAP}", "6":"6\N{COMBINING ENCLOSING KEYCAP}", "7":"7\N{COMBINING ENCLOSING KEYCAP}", "8":"8\N{COMBINING ENCLOSING KEYCAP}", "9":"9\N{COMBINING ENCLOSING KEYCAP}",
            "a":"\U0001F1E6", "b":"\U0001F1E7", "c":"\U0001F1E8", "d":"\U0001F1E9", "e":"\U0001F1EA", "f":"\U0001F1EB", "g":"\U0001F1EC", "h":"\U0001F1ED", "i":"\U0001F1EE", "j":"\U0001F1EF",
            "k":"\U0001F1F0", "l":"\U0001F1F1", "m":"\U0001F1F2", "n":"\U0001F1F3", "o":"\U0001F1F4", "p":"\U0001F1F5", "q":"\U0001F1F6", "r":"\U0001F1F7", "s":"\U0001F1F8", "t":"\U0001F1F9",
            "u":"\U0001F1FA", "v":"\U0001F1FB", "w":"\U0001F1FC", "x":"\U0001F1FD", "y":"\U0001F1FE", "z":"\U0001F1FF", " ":"\U000026aa"}

#entertainment
bliss = ["https://68.media.tumblr.com/ae10eb0ee90baff1ba03f3550779347c/tumblr_o38u8w0BXE1sksryco1_500.gif",
        "http://i.imgur.com/CdPpFns.gif",
        "http://i.imgur.com/MNy1f0c.gif",
        "http://pa1.narvii.com/6281/baa1196a1375fc230f32e423220aad504f9feb0f_hq.gif",
        "http://media.tumblr.com/tumblr_lzyo5jEt0O1qecah3o1_500.gif",
        "https://media.tenor.com/images/3090f7814cc27a9da60e752a0f7e1fe1/tenor.gif",
        "http://i.imgur.com/EqXsPHa.gif",
        "https://68.media.tumblr.com/b6e5fa651617ed3a7907f1f23d1c18f8/tumblr_opkaglYJNM1sk1rjvo1_500.gif",
        "http://pa1.narvii.com/5782/f71d840730510e4067111b1240484f34115e473f_hq.gif",
        ]
burn = ["http://media1.giphy.com/media/UD5oBoL8PanoQ/giphy.gif",
        "https://i.pinimg.com/originals/40/4a/c4/404ac4fc6f606605f87e0f6dce17e371.gif",
        "https://media.tenor.com/images/e57b700d3e915754861565542d865f01/tenor.gif",
        "https://memecrunch.com/meme/B5UVU/burn-it-with-fire/image.gif?w=400&c=1",
        "https://media.tenor.com/images/692d052ee377f19a69b374d238d75cb8/tenor.gif",
        "http://i.imgur.com/RRPco3Q.jpg",
        "http://68.media.tumblr.com/a5ae8eae466505b3910434e2b2cf10a4/tumblr_inline_ms2nwfXQd01qz4rgp.jpg",
        "http://data.whicdn.com/images/28490642/original.gif",
        "http://i.imgur.com/eVBQ2dT.gif",
        "http://img41.laughinggif.com/pic/HTTP2YuYXNzZXQuc291cC5pby9hc3NldC8zNzU0LzE4MjNfYzU0Ni5naWYlog.gif"
        ]

#utility
__utility = True
def __run(expression,char):
    expr2 = list()
    while char in expression:
        for i in range(len(expression)):
            if expression[i + 1] == char:
                if char == '+':
                    expr2.append(expression[i] + expression[i+2])
                if char == '*':
                    expr2.append(expression[i] * expression[i+2])
                if char == '/':
                    expr2.append(expression[i] / expression[i+2])
                if char == '^':
                    expr2.append(expression[i] ** expression[i+2])
                if i + 3 < len(expression):
                    for a in range(i + 3,len(expression)):
                        expr2.append(expression[a])
                break
            else:
                expr2.append(expression[i])
        expression = expr2 
        expr2 = list()
    if char == '+':    
        return(float(expression[0]))
    else:
        return(expression)
    
def run(expression,char):
    if __utility:
        return __run(expression,char)

def __brackclear(expression):
    lis=list(expression)
    expr2 = ""
    expr3 = ""
    pos1 = 0
    pos2 = 0
    extrabrack = 0
    if '(' in lis:
        for i in range(0, len(lis)):
            if lis[i] == '(':
                pos1 = i
                for a in range(i, len(lis)):
                    if lis[a] == '(':
                        extrabrack += 1
                    if lis[a] == ')':
                        pos2 = a
                        if extrabrack == 0:
                            break
                        else:
                            extrabrack -= 1
                break
        for i in range(0,pos1):
            expr2 += lis[i]
        if pos1 - 1 >= 0:
            if lis[pos1 - 1] not in ['-', '+', '/', '*', '^', '(']:
                expr2 += '*'
        for i in range(pos1 + 1,pos2):
            expr3 += lis[i]
        expr2 += str(__calculate(expr3))
        if pos2 + 1 < len(lis):
            if lis[pos2 + 1] not in ['-', '+', '/', '*', '^', ')']:
                expr2 += '*'
            for i in range(pos2 + 1, len(lis)):
                expr2 += lis[i]
        expr2 = brackclear(expr2)
        return(expr2)
    else:
        for i in lis:
            expr2 += i
        return(expr2)
    
def brackclear(expression):
    if __utility:
        return __brackclear(expression)

def __minclear(expression):
    expr2 = list()
    if '-' in expression:
        for i in range(0,len(expression)):
            if expression[i] == '-':
                expression[i + 1]=expression[i] + expression[i+1]
                if expression[i - 1] not in ['+', '/', '*', '^']:
                    expression[i] = '+'
                else:
                    expression[i] = None
    for i in range(0,len(expression)):
        if expression[i] == None:
            donothing()
        elif expression[i] not in ['+', '/', '*', '^']:
            expr2.append(float(expression[i]))
        else:
            expr2.append(expression[i])
    return(expr2)

def minclear(expression):
    if __utility:
        return __minclear(expression)

def __digits(expression):
    expr2 = [""]
    q = 0
    justnum = False 
    for i in range(0,len(expression)):
        if expression[i] not in ['-', '+', '/', '*', '^']:
            expr2[q] += expression[i]
            justnum=True 
        else:
            if justnum:
                justnum = False 
                expr2.append("")
                q += 1
            expr2[q] += expression[i]
            expr2.append("")
            q += 1
    return(expr2)

def digits(expression):
    if __utility:
        return __digits(expression)

def __eclear(expression):
    expression=list(expression)
    expr2=""
    for i in range(0,len(expression)):
        if expression[i]=='e':
            expression[i]=str(2.71828)
    for i in expression:
        expr2+=i
    return(expr2)

def eclear(expression):
    if __utility:
        return __eclear(expression)

def __calculate(expression):
    expression=eclear(expression)
    expression=brackclear(expression)
    expression=digits(expression)
    expression=minclear(expression)
    expression=run(expression, '/')
    expression=run(expression, '^')
    expression=run(expression, '*')
    return(run(expression, '+'))

def calculate(expression):
    if __utility:
        return __calculate(expression)
