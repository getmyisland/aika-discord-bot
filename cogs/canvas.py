import discord
from discord import app_commands
from discord.ext import commands
import requests


class CanvasCommands(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="horny", description="Gives the tagged user a horny license")
    async def horny(self, interaction: discord.Interaction, member: discord.Member):
        # Making a GET request to the endpoint
        resp = requests.get(f"https://some-random-api.ml/canvas/horny?avatar={member.avatar.url}")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            embed = discord.Embed(
                title=f"{member.name} now has a license to be horny"
            )
            embed.set_image(url=resp.url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code))

    @app_commands.command(name="simp_card", description="Gives the tagged user a simp card")
    async def simp_card(self, interaction: discord.Interaction, member: discord.Member):
        # Making a GET request to the endpoint
        resp = requests.get(f"https://some-random-api.ml/canvas/simpcard?avatar={member.avatar.url}")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            embed = discord.Embed(
                title=f"{member.name} now has a simp card"
            )
            embed.set_image(url=resp.url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code))

    @app_commands.command(name="no_bitches", description="Displays the given text in the no bitches meme")
    async def no_bitches(self, interaction: discord.Interaction, message: str):
        real_message = ''.join(e for e in message if e.isalnum() or e.isspace())

        # Making a GET request to the endpoint
        resp = requests.get(f"https://some-random-api.ml/canvas/nobitches?no={real_message}")
        # Checking if response has a healthy status code
        if 300 > resp.status_code >= 200:
            embed = discord.Embed(
                title=f"No Bitches?"
            )
            embed.set_image(url=resp.url)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("Received a bad status code of " + str(resp.status_code))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CanvasCommands(bot))
