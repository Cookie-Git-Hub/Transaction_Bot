import disnake
from disnake.ext import commands
import asyncio
from checker import coin_checker, transaction_checker, add_address_to_list, remove_address_from_list
from show_address_list import show_address_list

bot = commands.Bot(command_prefix="/",
                   intents=disnake.Intents.all(),
                   activity=disnake.Game('Waiting for tokens',
                   status=disnake.Status.online))

channel = 1106265730275622922
stop_flag = False

with open('help_message.txt', 'r', encoding='utf-8') as file:
    msg = file.read()

@bot.event
async def on_ready():
    print("The bot is ready!")

# @bot.slash_command(name='help', description='Bot description')
# async def help(inter):
#     await inter.response.send_message(msg)

@bot.slash_command(name='add', description='Add profile link')
async def add(inter, address):
    await inter.channel.send(add_address_to_list(address))

@bot.slash_command(name='remove', description='Remove profile link')
async def remove(inter, address):
    await inter.channel.send(remove_address_from_list(address))

@bot.slash_command(name='list', description='See address list')
async def help(inter):
    address_list = show_address_list() 
    await inter.response.send_message(address_list)
    
@bot.slash_command(name='start', description='Start checking transactions')
async def start(inter): 
    await inter.channel.send('**Monitoring started**')
    global stop_flag
    while not stop_flag: 
        bep_transactions =  coin_checker()
        transactions =  transaction_checker()  
        for transaction in bep_transactions:
            await inter.channel.send(transaction)
        for transaction in transactions:
            await inter.channel.send(transaction)
        await asyncio.sleep(60)

@bot.slash_command(name='stop', description='Stop monitoring transactions')
async def stop(inter):
    global stop_flag
    stop_flag = True
    await inter.channel.send('**Monitoring has been stoped**')
    

token = open('token.env', 'r').readline()
bot.run(token)