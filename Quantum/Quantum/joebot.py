#MTA0Mjc5NjYwMjI5ODk5ODg0Ng.GnGdgC.vQ_1XGJ6ai3eYT2XaNPvgLe6EvthhVx-RuBFd4

# This example requires the 'message_content' intent.

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.contains('$hello'):
        await message.channel.send('KOSOM AMR EL MOUGY')

client.run('MTA0Mjc5NjYwMjI5ODk5ODg0Ng.GnGdgC.vQ_1XGJ6ai3eYT2XaNPvgLe6EvthhVx-RuBFd4')
