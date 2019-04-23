import discord

from discord.ext import commands


class Echo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="echo")
	async def echo(self, ctx, *, content: str):
		print(content)
		await ctx.send(content)


def setup(bot):
	bot.add_cog(Echo(bot))
