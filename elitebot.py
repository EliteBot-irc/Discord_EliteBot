prefix='?'
myToken ='my token here'


import discord
from discord.ext import commands
from discord.ext.commands import Bot

# create an Intents object to enable the necessary events
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# create a new bot bot with a command prefix of '?'
bot = Bot(command_prefix=prefix, intents=intents)

# define a command that responds to the message '?hello'
@bot.command(name='hello')
async def say_hello(ctx):
    # check if the command was sent in a server/channel
    if isinstance(ctx.channel, discord.TextChannel):
        # check if the bot has permission to send messages in the channel
        if ctx.channel.permissions_for(ctx.me).send_messages:
            # send a message to the channel with the content 'Hello!'
            await ctx.send('Hello!')
        else:
            # send an error message in the channel if the bot does not have permission to send messages
            print('I don\'t have permission to send messages in this channel.')
    else:
        # send an error message in a DM if the command was not sent in a server/channel
        await ctx.author.send('This command can only be used in a server/channel.')

@bot.command(name='ping')
async def ping(ctx):
        embed = discord.Embed(
            title='🏓 Pong!',
            description=f'The bot latency is {round(self.bot.latency * 1000)}ms.',
            color=0x9C84EF
        )
        await ctx.send(embed=embed)        

# define an event that prints a message in the terminal when the bot is ready
@bot.event
async def on_ready():
    print('Connected to Discord!')

# run the bot with your Discord bot token
bot.run(myToken)
