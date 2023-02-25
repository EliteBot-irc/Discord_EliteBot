import discord
from discord.ext import commands

# create an Intents object to enable the necessary events
intents = discord.Intents.default()
intents.members = True

# create a new bot client with a command prefix of "?"
client = commands.Bot(command_prefix='?', intents=intents)

# define a command that responds to the message "?hello"
@client.command(name='hello')
async def say_hello(ctx):
    # check if the command was sent in a server/channel
    if isinstance(ctx.channel, discord.TextChannel):
        # check if the bot has permission to send messages in the channel
        if ctx.channel.permissions_for(ctx.me).send_messages:
            # send a message to the channel with the content "Hello!"
            await ctx.send('Hello!')
        else:
            # send an error message in the channel if the bot does not have permission to send messages
            print("I don't have permission to send messages in this channel.")
    else:
        # send an error message in a DM if the command was not sent in a server/channel
        await ctx.author.send('This command can only be used in a server/channel.')

# define an event that prints a message in the terminal when the bot is ready
@client.event
async def on_ready():
    print('Connected to Discord!')

# run the bot with your Discord bot token
client.run('your token here')
