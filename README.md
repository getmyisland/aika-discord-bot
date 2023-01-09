# discord-ai-bot

This Discord bot uses a small neural network to process user input and then using this information to respond dynamically to messages.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this bot locally you need Python3 and pip installed as well as the following pip packages. The version numbers behind show which versions I used, older or newer versions may also work.

```
discord == 1.7.3
requests == 2.28.0
nltk == 3.7
numpy == 1.23.2
tensorflow == 2.9.1
pandas == 1.4.3 
keras == 2.9.0
```

### Installing

Clone the git repository on your machine. Create a `.env` file inside the project folder. Discord requires a unique token for every bot. You can get the token on the [Discord Developer Portal](https://discord.com/developers/docs/intro) website, by creating a new application and copying the token.

Open the `.env` file in any text editor and paste in your token.

```
TOKEN=123456789
```

After following the steps above run this command inside the project folder.

```
python bot.py
```

You should now get messages that command modules have been loaded and that tensorflow trains the AI. 

## Built With

* [discord.py](https://discordpy.readthedocs.io/en/stable/) - Python Discord Framework
* [Tensorflow](https://www.tensorflow.org/) - Machine Learning Platform