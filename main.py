import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

class CreateClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == client.user:
            return

        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.lower().startswith('hello'):
            await message.channel.send('Hello!')

client = CreateClient()
client.run(TOKEN)