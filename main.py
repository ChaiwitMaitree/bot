import os
import discord
from discord.ext import commands
from discord import app_commands
from myserver import server_on

bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())





# คำสั่งBot พร้อมใช้งาน


@bot.event
async def on_ready():
    print("BOT Online!")


#แจ้งคนเข้าออก
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1272601097412018187)
    text = f"{member.name}ออกจากเชิฟเวอร์แล้ว!"

    emmbed = discord.embed (title = 'ออกจากเชิฟเวอร์แล้ว',description = 'ได้ออกจากเชิฟเวอร์แล้วนั้มโชคดีนั้ม',color = 7FFF00)
    await channel.send(embed = emmbed)
    await channel.send(text)

server_on()

bot.run(os.getenv(TOKEN))