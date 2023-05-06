import disnake
from disnake.ext import commands
from functions.transaction_checker import transaction_check
bot = commands.Bot(command_prefix="/",
                   intents=disnake.Intents.all(),
                   activity=disnake.Game('Waiting for tokens',
                   status=disnake.Status.online))

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.command(name='TC', description='Write your token')
async def TChecker(ctx:commands.Context, key, count=5):
    message = transaction_check(key, count) 
    await ctx.send(message)

@bot.command(name='tc', description='Write your token')
async def TChecker(ctx:commands.Context, key, count=5):
    message = transaction_check(key, count) 
    await ctx.send(message)

@bot.slash_command(name='help', description='Bot description')
async def help1(inter):
    msg = "[RUS]" + "\n" + "**Transaction Checker bot** - бот для отслеживания последних транзакций пользователя по его токену https://bscscan.com/." + "\n" + "Для вызова команды просмотра транзакций напишите “/TC” или “/tc”. Дальше через пробел укажите токен человека. После через ещё один пробел можно указать количество последних транзакций, которые хотите увидеть. По умолчанию эта опция имеет значение 5." + "\n" + "[ENG]" + "\n" + "**Transaction Checker bot** - a bot for tracking a user's latest transactions using his token https://bscscan.com/." + "\n" + "To call the transaction checker bot, type " + "/TC " + "or " + "/tc." + "\n" + "Next, after a space, write the person's token. After another space, you can specify the number of recent transactions you want to see. The default value of this option is 5."
    await inter.response.send_message(msg)

token = open('token.env', 'r').readline()
bot.run(token)



