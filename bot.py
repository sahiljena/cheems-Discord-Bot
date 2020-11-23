import discord
import requests
from discord.ext import commands
import json
import os
import random
import csv




client = commands.Bot(command_prefix = '$bork ')

TOKEN = os.environ.get('TOKEN')

@client.event
async def on_ready():
    print("CHEEMS RUNNIG ~~")

@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')

@client.command()
async def pong(ctx):
    await ctx.send('Huh stupid hooman -_- `ping pong ping pong` everyday')

@client.command()
async def hi(ctx):
    await ctx.send('Helmo Hooman! Bork Bork :dog:')

@client.command()
async def about(ctx):
    await ctx.send('>>> Ima bot Under development by Sahil Jena  & Open Source Community on Github https://github.com/sahiljena/cheems-Discord-Bot :sweat_drops:')

@client.command()
async def commands(ctx):
    await ctx.send(" `hi` `ping` `about` `doggo` `meme` `roast` ")


@client.command()
async def doggo(ctx):
    URL = "https://dog.ceo/api/breeds/image/random"

    r = requests.get(URL)
    r = json.loads(r.text)
    print(r['message'])
    #print(r.message)
    await ctx.send(r['message'])

@client.command()
async def meme(ctx):
    URL = "https://meme-api.herokuapp.com/gimme"
    r = requests.get(URL)
    r = json.loads(r.text)
    await ctx.send(r['url'])

@client.command(pass_context=True)
async def roast(ctx, member: discord.Member = None):
    if member:
        print(member.name)
        if member.name == "sahiljena":
            await ctx.send("hmm sorrym i cant roastm my hooman !!")
        else:
            f = open("roasts.txt","r")

            roasts = f.readlines()

            reply = f'''```diff
-{roasts[random.randint(0,len(roasts))]}
``` {member.mention}'''
            await ctx.send(reply)
    else:
        await ctx.send("Providm a valid username")


@client.command(pass_context=True)
async def todo(ctx,args = None,task = None):
    if args == "add":
        n = 1
        with open('todo.csv', 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                n += 1
        with open('todo.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([n, task])
            await ctx.send("To-do list updated")
    if args == "show":
        todoList = []
        with open('todo.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                st = "``` {} {} ```".format(row[0],row[1])
                print(st)
                todoList.append(st)
        for i in todoList:
            print(i)
        reply = ""
        for i in todoList:
            reply += i+" "
        print(reply)

        await ctx.send(reply)



client.run(TOKEN)

