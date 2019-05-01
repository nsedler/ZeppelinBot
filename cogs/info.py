import discord

from discord.ext import commands


class Info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="ping")
	async def ping(self, ctx):
		await ctx.send("Ping! {0: .2f} ms: ".format(self.bot.latency *1000))

	@commands.command(name="about", desciption="Gives some basic information about Zeppelin Bot")
	async def about(self, ctx):

		embed = discord.Embed(color=0xff0000)
		embed.set_author(name="Zeppelin Bot", url="https://github.com/nsedler/ZeppelinBot", icon_url = "http://onebigphoto.com/uploads/2011/11/zeppelin-on-fire.jpg  ")
		embed.add_field(name="Whats the point of ZeppelinBot?", value = "ZeppelinBot is a bot I 'm making to better learn python.", inline=False)
		embed.add_field(name="Why the name Zeppelin?", value = "Because zeppelin rocks, man.", inline = False)
		await ctx.send(embed=embed)


def setup(bot):
	bot.add_cog(Info(bot))
