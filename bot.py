import os

import discord

from src.event_handler import EventHandler
from utils import generate_uuid


client = discord.Client()
token = os.getenv('TOKEN')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    user_id = message.author
    content = message.content
    response = EventHandler.execute(content, user_id, generate_uuid())
    await message.channel.send(response)

client.run(token)
