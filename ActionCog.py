from typing import Optional
import os

import discord
from discord import Embed
from discord.ext import commands
import re

regex_discord_message_url = (
    '(?!<)https://(ptb.|canary.)?discord(app)?.com/channels/'
    '(?P<guild>[0-9]{18})/(?P<channel>[0-9]{18})/(?P<message>[0-9]{18})(?!>)'
)
regex_extra_url = (
    r'\?base_aid=(?P<base_author_id>[0-9]{18})'
    '&aid=(?P<author_id>[0-9]{18})'
    '&extra=(?P<extra_messages>(|[0-9,]+))'
)

class ExpandDiscordMessageUrl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        await dispand(message)





async def dispand(message):
    messages = await extract_message(message)
    mentioned = 'False'
    for m in messages:
        sent_messages = []

        mentioned = f'引用:{message.author.mention}さん' if mentioned == 'False' else None 
        if m.content or m.attachments:
            sent_message = await message.channel.send(content=mentioned,embed=compose_embed(m))
            sent_messages.append(sent_message)
        for attachment in m.attachments[1:]:
            embed = Embed()
            embed.set_image(
                url=attachment.proxy_url
            )
            sent_attachment_message = await message.channel.send(embed=embed)
            sent_messages.append(sent_attachment_message)

        for embed in m.embeds:
            sent_embed_message = await message.channel.send(content=mentioned,embed=embed)
            sent_messages.append(sent_embed_message)
    await message.delete()


async def extract_message(message):
    messages = []
    for ids in re.finditer(regex_discord_message_url, message.content):
        if message.guild.id != int(ids['guild']):
            continue
        fetched_message = await fetch_message_from_id(
            guild=message.guild,
            channel_id=int(ids['channel']),
            message_id=int(ids['message']),
        )
        messages.append(fetched_message)
    return messages


async def fetch_message_from_id(guild, channel_id, message_id):
    channel = guild.get_channel(channel_id)
    message = await channel.fetch_message(message_id)
    return message


def make_jump_url(base_message, dispand_message, extra_messages):
    return "{0.jump_url}?base_aid={1.id}&aid={2.id}&extra={3}".format(
        dispand_message,
        dispand_message.author,
        base_message.author,
        ",".join([str(i.id) for i in extra_messages])
    )


def from_jump_url(url):
    base_url_match = re.match(regex_discord_message_url + regex_extra_url, url)
    data = base_url_match.groupdict()
    return {
        "base_author_id": int(data["base_author_id"]),
        "author_id": int(data["author_id"]),
        "extra_messages": [int(_id) for _id in data["extra_messages"].split(",")] if data["extra_messages"] else []
    }


def compose_embed(message):
    embed = Embed(
        description=message.content,
        timestamp=message.created_at,
        colour=discord.Colour.blue()
    )
    embed.set_author(
        name=message.author.display_name,
        icon_url=message.author.avatar_url,
        url=message.jump_url
    )
    embed.set_footer(
        text=message.channel.name,
        icon_url=message.guild.icon_url,
    )
    if message.attachments and message.attachments[0].proxy_url:
        embed.set_image(
            url=message.attachments[0].proxy_url
        )
    return embed


def setup(bot):
    bot.add_cog(ExpandDiscordMessageUrl(bot))
