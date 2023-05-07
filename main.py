import disnake
from disnake.ext import commands
from functions.bsc_scan.bsc_checker import bsc_checker
bot = commands.Bot(command_prefix="/",
                   intents=disnake.Intents.all(),
                   activity=disnake.Game('Waiting for tokens',
                   status=disnake.Status.online))

client = disnake.Client()
channel_id = 1

with open('help_message.txt', 'r', encoding='utf-8') as file:
    msg = file.read()

@bot.slash_command(name='help', description='Bot description')
async def help1(inter):
    await inter.response.send_message(msg)

async def check_transactions():
    transactions = bsc_checker()
    channel = client.get_channel(channel_id)  
    await channel.send(transactions)

@client.event
async def on_ready():
    print("The bot is ready!")
    while True:
        await check_transactions()


token = open('token.env', 'r').readline()
bot.run(token)



