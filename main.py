import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

description = '''Example Bot'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=';', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print('[{0.guild.name}] Message from {0.author}: {0.content}'.format(message))

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')

bot.run(TOKEN)