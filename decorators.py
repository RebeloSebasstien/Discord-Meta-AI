from discord.ext import commands
from discord.ext.commands import Context


def AI_check():
    async def predicate(ctx: Context) -> bool:
        if ctx.me.guild_permissions.administrator:
            return True
        else:
            return False
    return commands.check(predicate)
