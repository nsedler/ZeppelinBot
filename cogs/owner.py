import discord
import sys

from discord.ext import commands


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(hidden=True)
	@commands.is_owner()
	async def quit(self, ctx):
		"""
		A command only for the owner, nate#9823, to shutdown the bot
		"""
		sys.exit(0)

	@commands.command(hidden=True)
	@commands.is_owner()
	async def guilds(self, ctx):
		pass

		desc = ""

		embed = discord.Embed(title="__**Guiilds**__", description="", color=0xff0000)

		embed.set_author(name="ZeppelinBot", url="https://github.com/nsedler/ZeppelinBot", icon_url="https://3iz4pu1r2cxqxc3i63gnhpmh-wpengine.netdna-ssl.com/wp-content/uploads/burning-with-mast.jpg")
		


def setup(bot):
	bot.add_cog(Owner(bot))