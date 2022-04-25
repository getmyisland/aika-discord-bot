import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import aiohttp

# Load the token
load_dotenv()
TOKEN = os.getenv('TOKEN')

command_prefix = '$'
description = '''Discord Bot made by GetMyIsland'''
intents = discord.Intents.default()
intents.members = True

# Create the bot
bot = commands.Bot(command_prefix=command_prefix, activity=discord.Game(name="with her Piggy"), status=discord.Status.offline, description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print('[{0.guild.name}] Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)


@bot.command(description="Talk with the bot")
async def talk(ctx, *content: str):
    await ctx.send('Coming Soon!')


@bot.command(description="Gives out a random fact")
async def fact(ctx):
    lines = open(os.getcwd() + '/resources/facts.txt').read().splitlines()
    random_line = random.choice(lines)
    fact = random_line.split(';')
    response = fact[0] + '\n' + '\n' + fact[1]
    await ctx.send(response)


@bot.command(description='Choose between a list of choices')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.reply(random.choice(choices))


@bot.command(description="Flip a coin")
async def coinflip(ctx):
    """Flip a coin."""
    coinside = random.randint(1, 2)

    if coinside == 1:
        await ctx.reply('Heads')
    else:
        await ctx.reply('Tails')


@bot.command(description="Lists all members with a specific role")
async def role(ctx, *role):
    role_name = " ".join(role)

    discord_role = discord.utils.get(ctx.guild.roles, name=role_name)

    if discord_role is not None:
        members = ''
        for member in discord_role.members:
            members = members + member.name + '\n'

        if members:
            embed = discord.Embed(
                title="Users with the role " + role_name,
                description=members
            )
            await ctx.reply(embed=embed)
        else:
            await ctx.reply("No user has the role " + role_name)
    else:
        await ctx.reply("There is no role with the name " + role_name)


bot.run(TOKEN)