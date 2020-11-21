import discord
import pandas as pd
import smtplib, ssl
import requests
from discord.ext import commands
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  
import json



client = commands.Bot(command_prefix = '$bork ')

TOKEN = 'NzYzNzkxODY0ODY4MjQxNDY5.X382mw.0TC-rnyhwSSaYm7IUUa7KhKtU1g'
df = pd.read_csv('users.csv') 
ALL_MEMBERS = []
for i,j in df.iterrows():
    temp = [j['username'],j['email']]
    ALL_MEMBERS.append(temp)
print(ALL_MEMBERS)

def send_mail(receiver_email,time):
    sender_email = "find.roomy.otp@gmail.com"
    message = MIMEMultipart("alternative")
    message["Subject"] = "INVITE : MLSA"
    message["From"] = 'find.roomy.otp@gmail.com'
    message["To"] = receiver_email
    html = ("""\
    <html>
        <body>
            <b><p style='color: blue;'>Meeting Scheduled at : <p style='color:red;'>{}</p></p></b>
        </body>
    </html>
    """).format(time)
    #turinig into mime content
    part2 = MIMEText(html, "html")

    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, "Sahil8139")
        server.sendmail(sender_email, receiver_email, message.as_string())


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
async def invite(ctx,args,args2):
    users = args
    users = users.split()
    time = args2
     #CSV file to read data from
    #await ctx.send("{},{}".format(users,time))
    #try:
    for i in users:
        for j in ALL_MEMBERS:
            if i == j[0]:
                send_mail(j[1],time)
    await ctx.send("Imvite Sent!")
    #except Exception as e:
    #     await ctx.send(e)
'''
@client.command()
async def testargs(ctx,*args):
    await ctx.send("{} , Username -> {}".format(len(args),args))
'''

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

