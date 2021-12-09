import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='"syro"'))

    async def on_message(self, message):

        msg = message.content.lower()

        # don't respond to ourselves
        if message.author == self.user:
            return

        if not msg[0:4] == 'syro':
          return # ignore if first four characters are not "syro"

        if msg == 'syro':
            await message.channel.send('you can always do it yourself, right?')
            return
        
        if 'can you give' in msg and 'feedback' in msg:
            await message.channel.send("Test cases did not work")
        
        if 'help' in msg:
            await message.channel.send("I won't help you with that because I expect you to be reading the textbook")


client = MyClient()
client.run(os.getenv("DISCORD_BOT_SECRET"))
