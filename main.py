import discord
import os
import random

def mute(member, muted=True):
  await member.edit(mute=muted)

def deafen(member, deafened=True):
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
    member = message.mentions[0]
    await member.edit(mute=True)
  
  if message.content.startswith('%deafen'):
    member = message.mentions[0]
    await member.edit(deafen=True)

  if message.content.startswith('%unmute'):
    member = message.mentions[0]
    await member.edit(mute=False)
  
  if message.content.startswith('%undeafen'):
    member = message.mentions[0]
    await member.edit(deafen=False)

client.run(os.getenv("TOKEN"))