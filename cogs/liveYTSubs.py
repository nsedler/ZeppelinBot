import discord
import json
import os

from discord.ext import commands
from urllib.request import urlopen


class YouTube(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.api_token = os.getenv("YTAPI")

	@commands.command(name="subs", description="live subcount of pewdiepie vs t-series")
	async def subs(self, ctx):
		jsonn_pewds = urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key={}".format(self.api_token))
		json_tseries = urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key={}".format(self.api_token))

		embed = discord.Embed(title="Pewdiepie vs T-Series", description="A live subcount of pewdiepie vs t-series", color=0xff0000)
		embed.set_thumbnail(
			url="https://i0.wp.com/culturedvultures.com/wp-content/uploads/2018/12/Her-ass-is-a-spaceship-I-want-to-ride._.jpg")
		embed.add_field(name="pewdiepie", value="{:,}".format(int(json.loads(jsonn_pewds.read())['items'][0]['statistics']['subscriberCount'])), inline=True)
		embed.add_field(name="t-series", value="{:,}".format(int(json.loads(json_tseries.read())['items'][0]['statistics']['subscriberCount'])), inline=True)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(YouTube(bot))