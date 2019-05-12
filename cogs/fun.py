import discord
import json
import os
import asyncio

from discord.ext import commands
from urllib.request import urlopen, Request


class Fun(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.api_token = os.getenv("YTAPI")


	async def cog_after_invoke(self, ctx):
		print("\n----------------------------")
		print("{0.author} used {0.command}...".format(ctx))
		print("----------------------------")


	@commands.command()
	async def subs(self, ctx):

		"""
		Live subcount of pewdiepie vs t-series
		"""

		jsonn_pewds = urlopen(
			"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=pewdiepie&key={}".format(
				self.api_token))
		json_tseries = urlopen(
			"https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername=tseries&key={}".format(
				self.api_token))

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


	@commands.group()
	async def cat(self, ctx):

		"""
		Random cat pictures
		"""

		if ctx.invoked_subcommand is None:
			embed = discord.Embed(title="Random Cat", description="Meow!", color=0xff0000)
			embed.set_image(url=json.loads(urlopen("http://aws.random.cat/meow").read())['file'])

			await ctx.send(embed=embed)


	@cat.command(name="fact")
	async def cat_fact(self, ctx):

		"""
		Random facts about cats
		"""

		req = Request("https://some-random-api.ml/facts/cat", headers={'User-Agent': 'Mozilla/5.0'})

		embed = discord.Embed(title="__**Cat Fact**__", description=json.loads(urlopen(req).read())['fact'], color=0xff0000)
		embed.set_author(name="ZeppelinBot", url="https://github.com/nsedler/ZeppelinBot", icon_url="https://3iz4pu1r2cxqxc3i63gnhpmh-wpengine.netdna-ssl.com/wp-content/uploads/burning-with-mast.jpg")

		await ctx.send(embed=embed)


	@commands.group()
	async def dog(self, ctx):

		"""
		Random dog pictures
		"""

		if ctx.invoked_subcommand is None:
			embed = discord.Embed(title="Random dog", description="Woof!", color=0xff0000)
			req = Request("https://some-random-api.ml/img/dog", headers={'User-Agent': 'Mozilla/5.0'})
			embed.set_image(url=json.loads(urlopen(req).read())['link'])

			await ctx.send(embed=embed)


	@dog.command(name="fact")
	async def dog_fact(self, ctx):

		"""
		Random facts about dogs
		"""

		req = Request("https://some-random-api.ml/facts/dog", headers={'User-Agent': 'Mozilla/5.0'})

		embed = discord.Embed(title="__**Dog Fact**__", description=json.loads(urlopen(req).read())['fact'], color=0xff0000)
		embed.set_author(name="ZeppelinBot", url="https://github.com/nsedler/ZeppelinBot", icon_url="https://3iz4pu1r2cxqxc3i63gnhpmh-wpengine.netdna-ssl.com/wp-content/uploads/burning-with-mast.jpg")

		await ctx.send(embed=embed)


	@commands.command()
	async def token(self, ctx):

		"""
		Get ZeppelinBots token
		"""

		req = Request("https://some-random-api.ml/bottoken", headers={'User-Agent': 'Mozilla/5.0'})

		embed = discord.Embed(title="__**Bot Token**__", description=json.loads(urlopen(req).read())['token'], color=0xff0000)
		embed.set_author(name="ZeppelinBot", url="https://github.com/nsedler/ZeppelinBot", icon_url="https://3iz4pu1r2cxqxc3i63gnhpmh-wpengine.netdna-ssl.com/wp-content/uploads/burning-with-mast.jpg")

		await ctx.send(embed=embed)


	@commands.command()
	async def bored(self, ctx):

		"""
		Finds you a random activity to do when bored
		"""

		req = Request("https://www.boredapi.com/api/activity?participants=1", headers={'User-Agent': 'Mozilla/5.0'})

		embed = discord.Embed(title="__**Activity to do**__", description=json.loads(urlopen(req).read())['activity'], color=0xff0000)
		embed.set_author(name="ZeppelinBot", url="https://github.com/nsedler/ZeppelinBot", icon_url="https://3iz4pu1r2cxqxc3i63gnhpmh-wpengine.netdna-ssl.com/wp-content/uploads/burning-with-mast.jpg")

		await ctx.send(embed=embed)


	@commands.command()
	async def insult(self, ctx, user: discord.Member):

		"""
		Insult @another_member
		"""

		req = Request("https://evilinsult.com/generate_insult.php?lang=en&type=json", headers={'User-Agent': 'Mozilla/5.0'})

		if user.id == 185063150557593600 or user.id == 569991046428098637:
    			await ctx.send(ctx.author.name + ", " + json.loads(urlopen(req).read())['insult'])
		else:
    			await ctx.send(user.name + ", " + json.loads(urlopen(req).read())['insult'])

	
	@commands.command()
	async def whois(self, ctx, *, member : discord.Member=None):

		user = member or ctx.author

		member_number = sorted(ctx.guild.members, key=lambda m: m.joined_at).index(user) + 1
		rolenames = ', '.join([r.name for r in user.roles if r.name != "@everyone"]) or 'None'

		embed = discord.Embed(description="{0.mention}".format(user), color=user.color)
		embed.set_author(name=user, icon_url=user.avatar_url)

		embed.add_field(name="Status", value="{0.status}".format(user), inline=True)
		embed.add_field(name="Joined", value=user.joined_at.strftime('%a, %b %d, %Y %I:%M %p'), inline=True)
		embed.add_field(name="Roles[{}]".format(len(user.roles) -1), value=rolenames, inline=False)
		embed.add_field(name="Join Position", value=member_number, inline=True)
		embed.add_field(name="Registered", value=user.created_at.strftime('%a, %b %d, %Y %I:%M %p'), inline=True)


		await ctx.send(embed=embed)
		

def setup(bot):
	bot.add_cog(Fun(bot))