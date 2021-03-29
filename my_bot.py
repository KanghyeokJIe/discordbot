#run.py
import discord
import youtube_dl
import asyncio, discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!") #접두사를 !로 지정

@bot.event
async def on_ready():
	print("We have logged in as {0.user}".format(bot))
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client)) #봇이 실행되면 콘솔창에 표시

@client.event
async def on_message(message):
    if message.author == client.user: # 봇 자신이 보내는 메세지는 무시
        return

    if message.content.startswith('!응애'): # 만약 !응애로 시작하는 채팅이 올라오면
        await message.channel.send('응애에요!') # 응애에요!라고 보내기

client.run('ODI1ODg4NjU2OTM3NzEzNjk0.YGEewA.HTksbVZjFSnK1IlJEA3WkNfQHEw') #토큰

@bot.command()  # 봇이 음성채널에 입장
async def play(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()  # 봇이 음성채널에서 퇴장
async def leave(ctx):
	await bot.voice_clients[0].disconnect()

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
    	await channel.connect()
    	await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))

    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))