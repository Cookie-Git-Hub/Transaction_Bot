import disnake
from disnake.ext import commands
import asyncio
from checker import coin_checker, transaction_checker, add_address_to_list, remove_address_from_list
from registration import user_registration

bot = commands.Bot(command_prefix="/",
                   intents=disnake.Intents.all(),
                   activity=disnake.Game('Waiting for tokens',
                   status=disnake.Status.online))

stop_flag = False

with open('help_message.txt', 'r', encoding='utf-8') as file:
    msg = file.read()

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.slash_command(name='help', description='bot description')
async def help(inter):
    await inter.response.send_message(msg)

@bot.slash_command(name='register', description='registration')
async def register(ctx):
    user_id = str(ctx.author.id)
    await user_registration(user_id)

@bot.slash_command(name='add', description='add profile link')
async def add(ctx, site_name, address):
    user_id = str(ctx.author.id)
    await ctx.send(add_address_to_list(user_id, site_name, address))

@bot.slash_command(name='remove', description='remove profile link')
async def remove(ctx, site_name, address):
    user_id = str(ctx.author.id)
    await ctx.send(remove_address_from_list(user_id, site_name, address))

# @bot.slash_command(name='list', description='see your profile list')
# async def help(inter):
#     user_id = str(ctx.author.id)
#     address_list = create_address_list(user_id) 
#     await inter.response.send_message(msg)
    
@bot.slash_command(name='start', description='start checking transactions')
async def start(ctx):
    user_id = str(ctx.author.id)  
    global stop_flag
    while not stop_flag: 
        bep_transactions =  coin_checker(user_id)
        transactions =  transaction_checker(user_id)  
        for transaction in bep_transactions:
            await ctx.author.send(transaction)
        for transaction in transactions:
            await ctx.author.send(transaction)
        await asyncio.sleep(60)

@bot.slash_command(name='stop', description='stop monitoring transactions')
async def stop(ctx):
    global stop_flag
    stop_flag = True
    await ctx.author.send('monitoring has been stoped')
    



token = open('token.env', 'r').readline()
bot.run(token)



