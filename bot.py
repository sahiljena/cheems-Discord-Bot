import discord
import pandas as pd
import smtplib, ssl
import requests
from discord.ext import commands
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
import json



client = commands.Bot(command_prefix = '$bork ')

TOKEN = ''

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
    await ctx.send(" `hi` `ping` `about` ")


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


client.run(TOKEN)

