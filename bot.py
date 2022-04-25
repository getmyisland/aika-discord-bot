import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import time

# Load the token
load_dotenv()
TOKEN = os.getenv('TOKEN')

command_prefix = '$'
description = '''Discord Bot made by GetMyIsland'''
intents = discord.Intents.default()
intents.members = True

# Create the bot
bot = commands.Bot(command_prefix=command_prefix, description=description, intents=intents)


# When the bot goes online
@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)
    # Setting `Playing ` status
    await bot.change_presence(activity=discord.Game(name="with her Piggy"))


# When a message gets send
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print('[{0.guild.name}] Message from {0.author}: {0.content}'.format(message))
    await bot.process_commands(message)

    if message.content.lower().startswith('hello'):
        await message.channel.send('Hello!')


@bot.command(description="Talk with the bot")
async def talk(ctx, *content: str):
    await ctx.send('Coming Soon!')


@bot.command(description='Choose between an unknown amount of choices')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))


@bot.command(description="Flip a coin")
async def coinflip(ctx):
    """Flip a coin."""
    coinside = random.randint(1, 2)

    if coinside == 1:
        await ctx.send('Heads')
    else:
        await ctx.send('Tails')


@bot.command(description="Gives out a random fact")
async def fact(ctx):
    lines = open(os.getcwd() + '/resources/facts.txt').read().splitlines()
    random_line = random.choice(lines)
    fact = random_line.split(';')
    response = fact[0] + '\n' + '\n' + fact[1]
    await ctx.send(response)


@bot.command(description="Rickroll your friends")
async def rickroll(ctx):
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable=os.getcwd() + "/resources/ffmpeg.exe", source=os.getcwd() + "/resources/rickroll.mp3"))
        ctx.delete()
    else:
        await ctx.send(str(ctx.author.name) + " is not in a voice channel.")


@bot.command(description="Leaves an existing voice channel")
async def leave(ctx):
    #Leaves the voice channel
    if ctx.author.voice.channel and ctx.author.voice.channel == ctx.voice_client.channel:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send('You have to be connected to the same voice channel to disconnect me.')


bot.run(TOKEN)