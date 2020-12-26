import discord
import os
import random
import time

run = True




async def mute(member, muted=True):
  await member.edit(mute=muted)

async def deafen(member, deafened=True):
  await member.edit(deafen=deafened)

client = discord.Client()

@client.event
async def on_ready():
  print("logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('%mute'):
    words = message.content.split(" ")
    member = message.mentions[0]
    amount = int(words[3])
    for i in range(amount):
      await mute(member)
      time.sleep(random.randint(10, 15))
      await mute(member, muted=False)
      time.sleep(random.randint(1, 3))

  
  if message.content.startswith('%deafen'):
    await deafen(message.mentions[0])
  
  if message.content.startswith('%undeafen'):
    await deafen(message.mentions[0], deafened=False)

client.run(os.getenv("TOKEN"))