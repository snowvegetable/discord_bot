from core.classes import *
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print("bot is online")


@bot.event
async def on_member_join(member):
    print(f"{member} join!")


@bot.event
async def on_member_remove(member):
    print(f"{member} leave!")


for FileName in os.listdir('./cmds'):
    if FileName.endswith('.py'):
        bot.load_extension(f"cmds.{FileName[:-3]}")

if __name__ == "__main__":
    bot.run(jdata["Token"])