import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.upper() == 'SYRO':
            await message.channel.send('you can always do it yourself, right?')
        
        if message.content.lower() == 'syro, can you help me with this?':
            await message.channel.send("I won't answer because I expect you to be reading the textbook")
        
        if message.content.lower() == 'syro, can you give me feedback so I can improve?':
          await message.channel.send("Test cases did not work")


client = MyClient()
client.run('ENTER TOKEN HERE')
