import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'bork ')

TOKEN = #TOKEN HERE

@client.event
async def on_ready():
    print("Hello , World")

@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')

@client.command()
async def hi(ctx):
    await ctx.send('Helmo Hooman! Bork Bork :dog:')

@client.command()
async def about(ctx):
    await ctx.send('>>> Ima bot Under development by :fire: shri shri Sahil Jena https://sahiljena.netlify.app/ sir :sweat_drops:')

@client.command()
async def command(ctx):
    await ctx.send(" `hi` `ping` `play` `food` `about` ")
client.run(TOKEN)