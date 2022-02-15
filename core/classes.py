import discord
from discord.ext import commands
import json

with open("setting.json", mode="r", encoding="utf-8") as data:
    jdata = json.load(data)


class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
