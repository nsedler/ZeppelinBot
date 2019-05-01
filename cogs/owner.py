import discord
import sys

from discord.ext import commands


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="quit", description="Shuts the bot down", hidden=True)
	@commands.is_owner()
	async def quit(self, ctx):
		"""
		A command only for the owner, nate#9823, to shutdown the bot
		"""
		sys.exit(0)


def setup(bot):
	bot.add_cog(Owner(bot))