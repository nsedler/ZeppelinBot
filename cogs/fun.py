import discord
import json
import os
import urllib

from discord.ext import commands
from urllib.request import urlopen, Request


class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.api_token = os.getenv("YTAPI")

	class AppURLopener(urllib.request.FancyURLopener):
		version = "Mozilla/5.0"

	@commands.command()
	async def subs(self, ctx):

		"""
		Live subcount of pewdiepie vs t-series
		"""

		jsonn_pewds = urlopen(
			"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key={}".format(self.api_token))
		json_tseries = urlopen(
			"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key={}".format(self.api_token))

		embed = discord.Embed(title="Pewdiepie vs T-Series", description="A live subcount of pewdiepie vs t-series", color=0xff0000)
		embed.set_thumbnail(
			url="https://i0.wp.com/culturedvultures.com/wp-content/uploads/2018/12/Her-ass-is-a-spaceship-I-want-to-ride._.jpg")
		embed.add_field(name="pewdiepie", value="{:,}".format(
			int(json.loads(jsonn_pewds.read())['items'][0]['statistics']['subscriberCount'])), inline=True)
		embed.add_field(name="t-series", value="{:,}".format(
			int(json.loads(json_tseries.read())['items'][0]['statistics']['subscriberCount'])), inline=True)
		await ctx.send(embed=embed)

	@commands.command()
	async def echo(self, ctx, *, content: str):
		"""
		Repeats what you say
		"""
		await ctx.send(content)

	@commands.command()
	async def meow(self, ctx):
		"""
		Random cat pictures
		"""
		embed = discord.Embed(title="Random Cat", description="Meow!", color=0xff0000)
		embed.set_image(url=json.loads(urlopen("http://aws.random.cat/meow").read())['file'])

		await ctx.send(embed=embed)

	@commands.command()
	async def woof(self, ctx):
		"""
		Random dog pictures
		"""
		embed = discord.Embed(title="Random dog", description="Woof!", color=0xff0000)
		req = Request("https://api-to.get-a.life/img/dog", headers={'User-Agent': 'Mozilla/5.0'})
		embed.set_image(url=json.loads(urlopen(req).read())['link'])

		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Fun(bot))