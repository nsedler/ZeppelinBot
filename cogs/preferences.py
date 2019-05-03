import discord
import json

from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


def open_json():
	with open("prefixes.json") as f:
		prefixes = json.load(f)
		return prefixes


def write_json(prefixes):
	with open('prefixes.json', 'w') as outfile:
		json.dump(prefixes, outfile)


class Preferences(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.group()
	@has_permissions(administrator=True)
	async def prefix(self, ctx):

		"""
		Allows you to view your guilds prefix
		"""

		if ctx.invoked_subcommand is None:
			guild_id = ctx.message.guild.id

			prefix = "."
			prefixes = open_json()

			for k, v in prefixes.items():
				if k == str(guild_id):
					prefix = v

			await ctx.send("Your guilds prefix is: " + prefix)

	@prefix.command()
	@has_permissions(administrator=True)
	async def set(self, ctx, prefix):

		"""
		Sets the prefix for the specific guild
		"""

		guild_id = ctx.message.guild.id
		prefixes = open_json()
		prefixes.update({str(guild_id): prefix})

		write_json(prefixes)

		await ctx.send("You have set your guilds prefix to: *" + prefix + "*")

	@prefix.command()
	@has_permissions(administrator=True)
	async def remove(self, ctx):

		"""
		Set the prefix of your guild to the default prefix
		"""

		guild_id = ctx.message.guild.id
		prefixes = open_json()

		try:
			prefixes.pop(str(guild_id))
			write_json(prefixes)
			await ctx.send("Your guilds prefix has been reset to: *.*")
		except Exception as e:
			await ctx.send("Your guilds prefix has been reset to: *.*")


def setup(bot):
	bot.add_cog(Preferences(bot))