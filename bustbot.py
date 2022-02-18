#!/usr/bin/env python3.8

import discord
import random
import os
import platform
from dotenv import load_dotenv

if("Linux" in platform.platform()):
    load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('Bust bot online'.format(client))

gaylebMessages = [
    'naw puttin the kids to bed',
    'in a meeting',
    'lmao',
    'thinkin about moving to georgia',
    'had to cut the mullet',
    'tane you watched daredevil yet',
    'cant talk watching encanto with the kids',
    'you guys done the lewdle yet',
    'u guys beat legends yet',
    #'yeah i\'d bang that dude no questions asked',
    'back in my hometown',
]

def getGaylebMessage():
    return gaylebMessages[random.randint(0,(len(gaylebMessages) - 1))]

def flip():
    res = ['Heads', 'Tails']
    return res[random.randint(0,1)]

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # get list of commands

    if message.content.startswith('!commands'):
        await message.channel.send('!test, !flip')
    # test online
    if message.content.startswith('!test'):
        await message.channel.send('bust bot online')

    # ------------    
    # bot functions    
    # ------------    
    
    if message.content.startswith('!flip'):
        await message.channel.send(flip())

    if 'cooch' in message.content.lower():
        await message.add_reaction("<:chadineau:943982782890262539>")

    if message.content.startswith('!gayleb'):
        await message.channel.send('gayleb says: ' + getGaylebMessage())
    

client.run(os.getenv('TOKEN'))