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


client = MyClient()
client.run('ENTER TOKEN HERE')
