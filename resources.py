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

heart = u"\u2764"
anger = u"\U0001F4A2"
white_tick = u"\u2705"
no_access = u"\U0001F6AB"


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
