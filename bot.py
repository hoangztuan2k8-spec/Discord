import os
import discord
from discord.ext import commands

# Khởi tạo cấu hình bot với quyền cơ bản
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Bot đã đăng nhập thành công dưới tên: {bot.user}")

# Lệnh kiểm tra trạng thái bot
@bot.command(name="status")
async def status(ctx):
    embed = discord.Embed(
        title="🖥️ Trạng Thái Hệ Thống Bot",
        description="Bot đang hoạt động ổn định và kết nối trực tuyến!",
        color=0x00FF00 # Màu xanh lá
    )
    embed.add_field(name="Độ trễ (Ping)", value=f"{round(bot.latency * 1000)}ms", inline=True)
    embed.add_field(name="Hệ thống", value="Được quản lý tự động qua GitHub", inline=True)
    await ctx.send(embed=embed)

# Chạy bot (Lấy token từ biến môi trường để bảo mật)
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("❌ Lỗi: Chưa tìm thấy DISCORD_BOT_TOKEN!")
  
