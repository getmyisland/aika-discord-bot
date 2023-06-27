# aika-discord-bot

The aika-discord-bot utilizes a neural network to process user input and then using this information to respond dynamically to messages. The bot is inspired by my dog Aika.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

To run this bot locally you need Python3 and pip installed. To install all required packages use the following command: `pip install -r requirements.txt`.

Tensorflow is not yet in the PyPI repositories and needs to be installed manually. If you have Python 3.10 installed you can use the command below to install it. Refer to the [official installation site](https://www.tensorflow.org/install/pip) for more installation options.

`python3 -m pip install --upgrade https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.11.0-cp310-cp310-win_amd64.whl`

### Installing

Clone the git repository on your machine. Discord requires a unique token for every bot. You can get the token on the [Discord Developer Portal](https://discord.com/developers/docs/intro) website, by creating a new application and copying the token.

Create a `.env` file inside the project folder. Open the `.env` file in any text editor and paste in your token.

`DISCORD_TOKEN=123456789`

After following the steps above run the command below at the root of the project folder.

`python bot.py`

You should now get messages that the cog modules have been loaded and Tensorflow trains the AI.

## Built With

* [discord.py](https://discordpy.readthedocs.io/en/stable/) - Python Discord Framework
* [Tensorflow](https://www.tensorflow.org/) - Machine Learning Platform
