import discord
from discord.ext import commands
import random
import math
import os
import asyncio

hostChannelID = os.environ.get('HOST_CHANNEL')
kchilID = os.environ.get('CREATOR_ID')

token = os.environ.get('DISCORD_BOT_TOKEN')
# invite link
# https://discord.com/api/oauth2/authorize?client_id=808868306676350976&permissions=68608&scope=bot

client = discord.Client()

bot = commands.Bot(command_prefix=">>")

@bot.event
async def on_ready():
    hostChannel = bot.get_channel(int(hostChannelID))
    kchilPing = "<@" + str(kchilID) + ">"
    await hostChannel.send(kchilPing + " I am online.")
    
@bot.command()
async def text(ctx):
    await ctx.send(str(hostChannelID))
    await ctx.send(type(hostChannelID))
    await ctx.send(str(kchilID))
    await ctx.send(type(kchildID))

@bot.command(aliases=["r"])
async def roll(ctx, numDice: int):
    resultTotal = 0
    resultText = ""
    successTotal = 0
    tensRolled = 0
    tenPairs = 0
    valueCritWin = 0
    totalSuccess = 0
    totalCritText = ""

    for r in range(numDice):
        tempResult = random.randint(1, 10)

        if tempResult >= 6:
            successTotal += 1

        if tempResult == 10:
            tensRolled += 1

        if r == 0:
            resultText = resultText + str(tempResult)
        elif r == 11:
            resultText = resultText + ",`\n`"
            resultText = resultText + str(tempResult)
        else:
            resultText = resultText + ", " + str(tempResult)

    resultText = "\n`Results: " + resultText + "`"

    tenPairs = math.floor(tensRolled / 2)
    valueCritWin = tenPairs * 2

    totalSuccess = successTotal + valueCritWin

    if totalSuccess <= 1:
        totalCritText = ""
    else:
        totalCritText = " (" + str(successTotal) + " + " + str(valueCritWin) + ")"

    await ctx.send("You rolled " + str(numDice) + "d10 for **" + str(totalSuccess) + "** successes." + totalCritText + resultText)

bot.run(token)
