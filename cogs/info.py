import discord

from discord.ext import commands


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ping")
	async def ping(self, ctx):
		await ctx.send("Ping! {0: .2f} ms: ".format(self.bot.latency *1000))

	@commands.command(name="about", desciption="Gives some basic information about Zeppelin Bot")
	async def about(self, ctx):
		pass


def setup(bot):
	bot.add_cog(Info(bot))
