import discord

from discord.ext import commands


class Echo(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="echo", description="Repeats what you say")
	async def echo(self, ctx, *, content: str):
		await ctx.send(content)


def setup(bot):
	bot.add_cog(Echo(bot))
