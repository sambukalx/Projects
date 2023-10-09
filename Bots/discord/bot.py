import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "?", intents = discord.Intents.all())
@bot.command(aliases = ["пинг", "ping"])
async def ping1(ctx):
    await ctx.send("pong!")
@bot.event
async def on_reade():
    print("I'm connected!")
@bot.event
async def on_message_edit(before, after):
    if before.content == after.content:
        return
    await before.channel.send(f"Ах ты нехороший человек \n{before.content} -> {after.content}")

bot.run("OTM3MzU5MTkyOTg0MDAyNjMw.Yfalxg.Ob6TlLIZaEkqJS1vH3VlzkvAWQo")
