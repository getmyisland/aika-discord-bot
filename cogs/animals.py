import discord
from discord import app_commands
from discord.ext import commands
import requests
from enum import Enum


class AnimalCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    class AnimalImages(Enum):
        Dog = "dog",
        Cat = "cat",
        Bird = "bird",
        Panda = "panda",
        Red_Panda = "red_panda",
        Fox = "fox",
        Koala = "koala",
        Racoon = "racoon",
        Kangaroo = "kangaroo",
        Whale = "whale"

    class AnimalFacts(Enum):
        Dog = "dog",
        Cat = "cat",
        Bird = "bird",
        Panda = "panda",
        Fox = "fox",
        Koala = "koala",

    @app_commands.command(name="animal_image", description="Sends a random image of the selected animal")
    async def animal_image(self, interaction: discord.Interaction, animal: AnimalImages):
        animal_name = ''.join(e for e in animal.value if e.isalnum())

        # Making a GET request to the endpoint
        resp = requests.get(f"https://some-random-api.ml/img/{animal_name}")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title=f"Random {animal_name} picture"
            )
            embed.set_image(url=content['link'])
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code))

    @app_commands.command(name="animal_fact", description="Sends a random fact of the selected animal")
    async def animal_fact(self, interaction: discord.Interaction, animal: AnimalFacts):
        animal_name = ''.join(e for e in animal.value if e.isalnum())

        # Making a GET request to the endpoint
        resp = requests.get(f"https://some-random-api.ml/facts/{animal_name}")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            content = resp.json()
            embed = discord.Embed(
                title=f"Random {animal_name} fact",
                description=content['fact']
            )
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AnimalCommands(bot))
