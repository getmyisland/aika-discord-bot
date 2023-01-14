import discord
from discord import app_commands
from discord.ext import commands
import random
import requests


class MiscCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(
        name="sync",
        description="Synchronises slash cogs with the Discord API"
    )
    async def sync(self, ctx) -> None:
        if not ctx.author.guild_permissions.administrator:
            await ctx.reply(f"You don't have the rights to use this command.", delete_after=10)
            return

        try:
            synced = await self.bot.tree.sync()
            await ctx.reply(f"Synced {len(synced)} command(s)", delete_after=10)
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)

    @app_commands.command(name="joke", description="Sends a random joke")
    async def joke(self, interaction: discord.Interaction) -> None:
        resp = requests.get(f"https://some-random-api.ml/joke")
        if 300 > resp.status_code >= 200:
            content = resp.json()
            await interaction.response.send_message(content['joke'])
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code), ephemeral=True)

    @app_commands.command(name="choose", description="Chooses between multiple choices")
    async def choose(self, interaction: discord.Interaction, choice1: str, choice2: str, choice3: str = None, choice4: str = None, choice5: str = None) -> None:

        choices = [choice1, choice2]

        if choice3 is not None:
            choices.append(choice3)

        if choice4 is not None:
            choices.append(choice4)

        if choice5 is not None:
            choices.append(choice5)

        # Chooses between multiple choices
        await interaction.response.send_message(random.choice(choices))

    @app_commands.command(name="coinflip", description="Flip a coin")
    async def coinflip(self, interaction: discord.Interaction) -> None:
        # Flip a coin
        coin_side = random.randint(1, 2)

        if coin_side == 1:
            await interaction.response.send_message('Heads')
        else:
            await interaction.response.send_message('Tails')

    @app_commands.command(name="base64_encode", description="Encode text into Base64")
    async def base64_encode(self, interaction: discord.Interaction, encode: str) -> None:
        resp = requests.get(f"https://some-random-api.ml/base64?encode={encode}")
        if 300 > resp.status_code >= 200:
            content = resp.json()
            await interaction.response.send_message(content['base64'])
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code), ephemeral=True)

    @app_commands.command(name="base64_decode", description="Decode text from Base64")
    async def base64_decode(self, interaction: discord.Interaction, decode: str) -> None:
        resp = requests.get(f"https://some-random-api.ml/base64?decode={decode}")
        if 300 > resp.status_code >= 200:
            content = resp.json()
            await interaction.response.send_message(content['text'])
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code), ephemeral=True)

    @app_commands.command(name="binary_encode", description="Encode text into Binary")
    async def binary_encode(self, interaction: discord.Interaction, encode: str) -> None:
        resp = requests.get(f"https://some-random-api.ml/binary?encode={encode}")
        if 300 > resp.status_code >= 200:
            content = resp.json()
            await interaction.response.send_message(content['binary'])
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code), ephemeral=True)

    @app_commands.command(name="binary_decode", description="Decode text from Binary")
    async def binary_decode(self, interaction: discord.Interaction, decode: str) -> None:
        resp = requests.get(f"https://some-random-api.ml/binary?decode={decode}")
        if 300 > resp.status_code >= 200:
            content = resp.json()
            await interaction.response.send_message(content['text'])
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code), ephemeral=True)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MiscCommands(bot))
