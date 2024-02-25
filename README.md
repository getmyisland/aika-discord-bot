# aika-discord-bot

A Discord bot, inspired by my dog Aika, that uses a neural network to respond to the user, built with [discord.py](https://discordpy.readthedocs.io/en/stable/).

## Features

* Neural Network
* Customizable Intents
* Miscellaneous Commands using [Some Random Api](https://some-random-api.com/)

## How To Use

To clone this application, you'll need [Git](https://git-scm.com/downloads) installed on your computer. From your command line:

```
# Clone this repository
$ git clone https://github.com/getmyisland/aika-discord-bot.git

# Go into the repository
$ cd aika-discord-bot
```

Create a `.env` file inside the repository folder and paste your bot token, which you received from the [Discord Developer Portal](https://discord.com/developers/applications), to this file as follows:

```
DISCORD_TOKEN=123YOUR456TOKEN789
```

### Docker (Recommended)

You need [Docker](https://www.docker.com/) installed on your computer. From your command line:

```
# Create and start the Docker container
$ sudo docker-compose up
```

### Without Docker

You need [Python3](https://www.python.org/downloads/) installed on your computer. From your command line:

```
# Install all requirements
pip install --no-cache-dir -r requirements.txt

# Run the bot
python3 bot.py
```

## Built With

* [discord.py](https://discordpy.readthedocs.io/en/stable/) - Python Discord Framework
* [Tensorflow](https://www.tensorflow.org/) - Machine Learning Platform
