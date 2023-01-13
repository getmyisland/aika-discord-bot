import string
import discord
from discord import app_commands
from discord.ext import commands
# from cogs.ai.ai import get_response


class TalkCommand(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="talk", description="Talk with me")
    async def talk(self, interaction: discord.Interaction, message: str) -> None:
        message = [letters.lower() for letters in message if letters not in string.punctuation]
        message = ''.join(message)
        texts = [message]

        await interaction.response.send_message("This command is currently disabled")
        # await interaction.response.send_message(get_response(self, texts))


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TalkCommand(bot))
