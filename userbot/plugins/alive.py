"""Check if userbot alive."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`Jarvis🤖 at your service Sire \n   【Lone☄Wolf】^.^ \nJab Tak Ye Telegram delete nahi hota㋡\nApun Idharich Rahenga!!😤\n Aaur tumhara bot sidha chalrela hain\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\n`\n"
                     "`Database Status: Databases functioning normally!\nApun Hamesha Tere Sath Rahenga, boleto master!\n`"
                     "")
