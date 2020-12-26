import Discord
import os
import random


client = Discord.Client()

@client.event
async def on_ready():
  print("logged in as {0.user}".format(client))

@client.event
async def on_message():
  if message.author == client.user:
    return
  
  if message.startswith('$mute'):
    while run == True:
    time.sleep(random.randint())      


client.run(os.getenv("TOKEN"))