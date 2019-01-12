import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '-')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Dynasty Beak | Prefix "-"'))
    print('Ready to Game') 


@client.event
async def on_message(message):
    if message.content == '-creator':
        await client.send_message(message.channel,'@ProLuckGaming#0001!')
    if message.content == '-credits':
        await client.send_message(message.channel,'@ProLuckGaming#0001!')
    if message.content.startswith('-gamemode'):
        randomlist = ["***Save The World***","***Battle Royale***",]
    if message.content.startswith('-jailbreak'):
        randomlist = ["***Go Criminal! Let's Steal Some Bills  :money_with_wings: :money_mouth: ***","***Go Police! No One Should Leave THE JAIL :police_car: :cop:  ***",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('-mode'):
        randomlist = ["***Solo***","***Duos***","***Squads***","***Playground***","Creative",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('-jump'):
        randomlist = ["**Jump To:_Tilted Towers_**","**Jump to:_Retail Row_**","**Jump to:_Greasy Grove_**","**Jump to:_Leaky Lake_**","***Go Die In The Sea (Unlucky)***"]
        await client.send_message(message.channel,(random.choice(randomlist))) 
    if message.content == '-ping':
        await client.send_message(message.channel,'Please Use ?ping For Dyno Bot :)')
client.run('NTMzMDA4OTgxNDMwNjMyNDU4.Dxky8Q.-M_pBwPZsXcAqA_fO100OY2ZskY')
