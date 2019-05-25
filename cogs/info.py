import discord

from discord.ext import commands


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	async def cog_after_invoke(self, ctx):
		print("\n----------------------------")
		print("{0.author} used {0.command}...".format(ctx))
		print("----------------------------")

	@commands.command(name="ping")
	async def ping(self, ctx):
		"""
		Ping of ZeppelinBot
		"""
		await ctx.send("Ping! {0: .2f} ms: ".format(self.bot.latency *1000))

	@commands.command(name="about")
	async def about(self, ctx):
		"""
		Basic information about ZeppelinBot
		"""
		embed = discord.Embed(color=0xff0000)
		embed.set_author(name="Zeppelin Bot", url="https://github.com/nsedler/ZeppelinBot", icon_url = "http://onebigphoto.com/uploads/2011/11/zeppelin-on-fire.jpg  ")
		embed.add_field(name="Whats the point of ZeppelinBot?", value = "ZeppelinBot is a bot I 'm making to better learn python.", inline=False)
		embed.add_field(name="Why the name Zeppelin?", value = "Because zeppelin rocks, man.", inline = False)
		await ctx.send(embed=embed)

	@commands.command()
	async def whois(self, ctx, *, member : discord.Member=None):

		"""
		Get info about @another_member (leave args blank for info about you)
		"""

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


	@commands.command()
	async def guild(self, ctx):

		"""
		Get the information about your guild
		"""

		guild = ctx.guild

		embed = discord.Embed(color=ctx.author.color)

		embed.set_author(name=guild.name, icon_url=guild.icon_url)
		embed.add_field(name="Owner", value=guild.owner.mention)
		embed.add_field(name="Guild Size", value=len(guild.members))
		embed.add_field(name="Guild Prefix", value=ctx.prefix)
		embed.add_field(name="Total Channels", value=len(guild.channels))
		embed.add_field(name="Text Channels", value=len(guild.text_channels))
		embed.add_field(name="Voice Channels", value=len(guild.voice_channels))
		

		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Info(bot))
