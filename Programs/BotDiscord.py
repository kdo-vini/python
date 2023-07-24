import discord
from discord.ext import commands
from pytube import YouTube
import os
import ffmpeg

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.command()
async def entrar(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send('Cheguei!')

@bot.command()
async def sair(ctx):
    voice_client = ctx.voice_client
    if voice_client:
        await voice_client.disconnect()
        await ctx.send('té mais!')
    else:
        await ctx.send("Eu não estou conectado a nenhum canal de voz!")

@bot.command()
async def tocar(ctx, url: str):
    if ctx.voice_client is None:
        if not ctx.author.voice:
            await ctx.send("{} não está conectado a um canal de voz.".format(ctx.author.name))
            return
        else:
            channel = ctx.author.voice.channel
            await channel.connect()

    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4").first()
    stream.download(filename="song.mp4")

    input_file = "song.mp4"
    output_file = "song.mp3"

    ffmpeg.input(input_file).output(output_file).run()

    voice_client = ctx.voice_client
    voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=output_file))

@bot.command()
async def pause(ctx):
    voice_client = ctx.voice_client

    if voice_client.is_playing():
        voice_client.pause()
        await ctx.send("A música foi pausada.")
    else:
        await ctx.send("A música já está pausada!")

@bot.command()
async def resume(ctx):
    voice_client = ctx.voice_client

    if voice_client.is_paused():
        voice_client.resume()
        await ctx.send("A música foi retomada.")
    else:
        await ctx.send("A música já está sendo tocada!")

bot.run('MTEzMTU4MDcwODQ5ODk4MDg3NA.GX2MQm.SeuYNxPiIBbMqOc8lfwdbZIILZhczBB_4JDrig')
