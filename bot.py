import discord
import requests
from discord.ext import commands
import json
import os
import random



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
async def command(ctx):
    await ctx.send(" `hi` `ping` `about` `doggo` `meme` ")


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

@client.command()
async def roast(ctx, *members: discord.Member = None):
    if members:
        f = open("roasts.txt","r")

        roasts = f.readlines()

        reply = f'''
        ```diff
        - {roasts[random.randint(0,len(roasts))]}
        ``` {' '.join([i.mention for i in members])}
        '''
        await ctx.send(reply)
    else:
        await ctx.send("Providm a valid username")

client.run(TOKEN)

