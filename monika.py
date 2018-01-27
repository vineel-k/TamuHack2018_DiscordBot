import discord
from discord.ext import commands

bot = commands.Bot(description="Short desc of your bot", command_prefix="!")

@bot.command()
async def ping():
    await bot.say("Pong!") 
@bot.command(pass_context=True)
async def say(ctx, *, something):
	await bot.say(something)
	await bot.delete_message(ctx.message)

bot.run('NDA2OTI5NDIxNzk5NTIyMzA0.DU6GIg.9rZZTRcR_6l0CcmYR_RLQAOXMMk')