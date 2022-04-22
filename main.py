import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

command_prefix = '$aika'
description = '''Discord Bot made by GetMyIsland'''
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        await guild.system_channel.send('Welcome {0.mention} to {1.name}!'.format(member, guild))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print('[{0.guild.name}] Message from {0.author}: {0.content}'.format(message))

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

bot.run(TOKEN)