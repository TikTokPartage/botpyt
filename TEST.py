import code
import os


os.system('cls')
import discord

import time
os.system("TEST BOT BY QDE#4156")
from colorama import Fore, Back, Style
from discord.ext.commands import Bot
from discord.ext import commands
int()
from pystyle import *

client = discord.Client()
time.sleep(2)
token="OTk1NDYwNjg1ODUxMDEzMjEy.GG8y-r.Y56j_Y_-Eh0p6-cQzWLNmDeb5eIwBwAiDWcURM"
print("Merci!")
time.sleep(5)
os.system('cls')
prefix="!"
bot = commands.Bot(command_prefix="!", description="Bot By Qde#4156🙂🙂🙂🙂🙂")
os.system('cls')
@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content == "paypal.me/Xsiroxtwitch":
        await message.delete()
        await message.channel.send("Les paypalme ne sont pas autorisé cheh @<955510155431256185>")

    if message.content == "paypal.me/xsiroxtwitch":
        await message.delete()
        await message.channel.send("Les paypalme ne sont pas autorisé cheh @<955510155431256185>")

    if message.content == "PayPal.me/xsiroxtwitch":
        await message.delete()
        await message.channel.send("Les paypalme ne sont pas autorisé cheh @<955510155431256185>")


    if message.content == "Paypal.me/Xsiroxtwitch":
        await message.delete()
        await message.channel.send("Les paypalme ne sont pas autorisé cheh @<955510155431256185>")

    
    
    
    
    
@client.event
async def on_ready():   
    os.system('cls')
    print(f'Merci davoir download le programme, pour rappel votre bot est co en tant que: {client.user} ')
    print("Votre bot est en ligne Félicitation, pour voir les commandes fait le préfix+help")
    print("votre prefix est:" + prefix)
client.run(token)