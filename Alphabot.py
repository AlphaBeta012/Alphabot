import discord
from discord.ext import commands
import os
import random

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print("bot is ready!")
    
@client.command()
async def ping(ctx):
    await ctx.send('pong!')

@client.command()
async def meme(ctx):
        image = os.listdir('/storage/emulated/0/image_meme/')
        imgString = random.choice(image)  
        path = "/storage/emulated/0/image_meme/" + imgString
        await ctx.send(file=discord.File(path))
                                                        
client.run('ODczMzQwNTAwNDM2OTc5NzQz.YQ2_uQ.kZda4utc_y94ukEd8g3ZuwMYopA')
