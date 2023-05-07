import disnake
from disnake.ext import commands
import time
from functions.bsc_scan.bsc_checker import bsc_checker, add_address_to_list, remove_address_from_list
bot = commands.Bot(command_prefix="/",
                   intents=disnake.Intents.all(),
                   activity=disnake.Game('Waiting for tokens',
                   status=disnake.Status.online))

client = disnake.Client()
channel_id = 1039967131518910476

with open('help_message.txt', 'r', encoding='utf-8') as file:
    msg = file.read()

@bot.slash_command(name='help', description='Bot description')
async def help(inter):
    await inter.response.send_message(msg)

@bot.slash_command(name='add', description='add profile link')
async def add(ctx, address):
    await ctx.send(add_address_to_list(address))

@bot.slash_command(name='remove', description='remove profile link')
async def remove(ctx, address):
    await ctx.send(remove_address_from_list(address))

@bot.event
async def on_ready():
    print("The bot is ready!")
    while True: 
        transactions = bsc_checker()
        channel = bot.get_channel(channel_id)  
        for transaction in transactions:
            await channel.send(transaction)
        time.sleep(60)

token = open('token.env', 'r').readline()
bot.run(token)



