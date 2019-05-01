import discord
import json

from discord.ext import commands

def open_json():
	with open("prefixes.json") as f:
		prefixes = json.load(f)

def write_json():
	with open('prefixes.json', 'w') as outfile:
		json.dump(prefixes, outfile)

class Preferences(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="prefix")
	async def prefix(self, ctx, arg1, prefix):

		guild_id = ctx.message.guild.id

		if arg1 == "set":


			prefixes.update({str(guild_id) : prefix})


		elif arg1 == "" or arg1 is None:
			ctx.send()





def setup(bot):
	bot.add_cog(Preferences(bot))