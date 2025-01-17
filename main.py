from discord.ext import commands
from dotenv import load_dotenv
import discord
import os
import asyncio

def setup_intents() -> None:
    intents = discord.Intents.default()
    intents.members = True
    intents.messages = True
    intents.guilds = True
    intents.reactions = True
    intents.message_content = True
    return intents

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!', intents=setup_intents())

@bot.event
async def on_ready() -> None:
    print(f'{bot.user.name} has connected to Discord!')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.load_extension("start"))
    loop.run_until_complete(bot.run(TOKEN))