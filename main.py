# Dependencies
import discord

# Local Dependencies
from resources import secret as Secret
from resources import handler as Handler
from resources.utils import setup as setup

setup.startRoutine()

client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    Handler.MessageHandler(message)



client.run(Secret.API_KEY)