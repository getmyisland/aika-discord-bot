import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')

command_prefix = '$'
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
    await bot.process_commands(message)

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')


@bot.command(description='Add two values together')
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command(description='Subtract the second value from the first')
async def subtract(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)


@bot.command(description='Choose between an unknown amount of choices')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command(description='Flip a coin')
async def coinflip(ctx):
    """Flip a coin."""
    coinside = random.randint(1, 2)

    if coinside == 1:
        await ctx.send('Heads')
    else:
        await ctx.send('Tails')


@bot.command(description="Gives out a random fact")
async def fact(ctx):
    lines = open('facts.txt').read().splitlines()
    random_line = random.choice(lines)
    fact = random_line.split(';')
    response = fact[0] + '\n' + '\n' + fact[1]
    await ctx.send(response)


@bot.command(description="See all commands")
async def commands(ctx):
    await ctx.send('Coming Soon!')

bot.run(TOKEN)