import discord
import sys

from discord.ext import commands


class Owner(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	async def cog_after_invoke(self, ctx):
		print("\n----------------------------")
		print("{0.author} used {0.command}...".format(ctx))
		print("----------------------------")

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
		"""
		A command only for the owner, nate#9823, to view all guilds ZeppelinBot is a member of
		"""

		desc = ""
		for g in self.guilds:
			desc += g.name + "\n"

		embed = discord.Embed(title="__**Guiilds**__", description=desc, color=0xff0000)

		embed.set_author(name="ZeppelinBot", url="https://github.com/nsedler/ZeppelinBot", icon_url="https://3iz4pu1r2cxqxc3i63gnhpmh-wpengine.netdna-ssl.com/wp-content/uploads/burning-with-mast.jpg")
		await ctx.send(embed=embed)
		


def setup(bot):
	bot.add_cog(Owner(bot))