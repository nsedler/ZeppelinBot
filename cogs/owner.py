import discord
import sys

from discord.ext import commands


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="quit", description="Shuts the bot down")
	@commands.is_owner()
	async def quit(self, ctx):
		sys.exit(0)


def setup(bot):
	bot.add_cog(Owner(bot))