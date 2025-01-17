
from discord.ext import commands
from processing import on_bot_start_command
from sharedfuncs import send_bot_embed
from better_profanity import profanity

class StartAI(commands.Cog):
    store_data = {}

    def __init__(self, bot):
        self.bot = bot
        self.is_started = False

    @commands.command(name="start")
    async def start(self, ctx):
        await send_bot_embed(ctx, description="Starting AI...")
        if not self.is_started:
            self.is_started = True
            await on_bot_start_command(ctx)
        else:
            await send_bot_embed(ctx, description="AI is already started.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if not self.is_started:
            return
        if message.author == self.bot.user:
            return
        if message.author.id not in StartAI.store_data:
            message.content = profanity.censor(message.content)
            StartAI.store_data[message.author.id] = "Message: " + message.content
        else:
            message.content = profanity.censor(message.content)
            StartAI.store_data[message.author.id] = StartAI.store_data[message.author.id] + ", Message: " + message.content

    @commands.Cog.listener()
    async def on_command_error(self, _, error):
        StartAI.clear_data()
        raise error

    @classmethod
    def get_data(cls):
        return cls.store_data
    
    @classmethod
    def clear_data(cls):
        cls.store_data = {}
        
async def setup(bot):
    await bot.add_cog(StartAI(bot))