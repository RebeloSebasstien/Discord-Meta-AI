from dataclasses import dataclass
from discord.ext.commands import Context
from decorators import AI_check
from sharedfuncs import make_embed
import random
import discord

@dataclass
class Action:
    user: discord.Member
    context: Context
    user_score: int

    @AI_check()
    async def mute_user(self) -> None:
        """Mutes the user."""
        await self.user.edit(mute=True)

    @AI_check()
    async def kick_user(self) -> None:
        """Kicks the user."""
        await self.user.kick()

    @AI_check()
    async def ban_user(self) -> None:
        """Bans the user."""
        await self.user.ban()

    @AI_check()
    async def unmute_user(self) -> None:
        """Unmutes the user."""
        await self.user.edit(mute=False)
    
    @AI_check()
    async def deafen_user(self) -> None:
        """Deafens the user."""
        await self.user.edit(deafen=True)

    @AI_check()
    async def undeafen_user(self) -> None:
        """Undeafens the user."""
        await self.user.edit(deafen=False)

    @AI_check()
    async def disconnect_user(self) -> None:
        """Disconnects the user."""
        await self.user.move_to(None)

    @AI_check()
    async def move_user(self) -> None:
        """Moves the user to another voice channel."""
        await self.user.move_to(random.choice(self.context.guild.voice_channels))

    @AI_check()
    async def delete_user_call(self) -> None:
        """Deletes the user's call."""
        user_call = self.user.voice
        await user_call.channel.delete()

    @AI_check()
    async def mute_every_user(self) -> None:
        """Mutes every user in the voice channel."""
        for member in self.user.voice.channel.members:
            await member.edit(mute=True)

    @AI_check()
    async def deafen_every_user(self) -> None:
        """Deafens every user in the voice channel."""
        for member in self.user.voice.channel.members:
            await member.edit(deafen=True)

    @AI_check()
    async def disconnect_every_user(self) -> None:
        """Disconnects every user in the voice channel."""
        for member in self.user.voice.channel.members:
            await member.move_to(None)
    @AI_check()
    async def warm_user(self) -> None:
        """Warns the user."""
        await self.context.send(f":warning: {self.user.mention} has been warned for being disrespectful. :warning:")

    @AI_check()
    async def give_user_random_role(self) -> None:
        """Gives the user a random role."""
        all_roles = self.context.guild.roles
        bot_role = self.context.guild.me.top_role
        valid_roles = [role for role in all_roles if role < bot_role]
        await self.user.add_roles(random.choice(valid_roles))

    @AI_check()
    async def change_channel_bitrate(self) -> None:
        """Changes the channel's bitrate."""
        await self.user.voice.channel.edit(bitrate=random.randint(8000, 96000))

    async def get_commands_dict(self) -> dict:
        """Returns a dictionary of all the commands and their respective weights."""
        return {
            0: [self.give_user_random_role],
            10: [self.unmute_user, self.undeafen_user],
            20: [self.warm_user],
            30: [self.change_channel_bitrate],
            40: [self.move_user],
            50: [self.mute_user, self.deafen_user],
            60: [self.disconnect_user],
            70: [self.deafen_every_user, self.mute_every_user],
            80: [self.delete_user_call, self.disconnect_every_user],
            90: [self.kick_user],
            100: [self.ban_user]
        }
    
    async def get_random_action(self) -> None:
        """Gets a random action based on the user's score."""
        commands = await self.get_commands_dict()
        for key in commands.keys():
            if self.user_score == key:
                action = random.choice(commands[key])
                description = f":robot: AI used action on **{self.user.name}**\n :magnet: Action: **{action.__name__}**\n :anger: Anger: **{self.user_score}%**"
                try:
                    await action()
                    return
                finally:
                    embed = await make_embed(description=description)
                    await self.context.send(embed=embed)
        