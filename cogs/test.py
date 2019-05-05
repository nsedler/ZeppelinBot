import discord

from discord.ext import commands


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.group()
	async def group1(self, ctx):
		await ctx.send("group1")

	@group1.command()
	async def test(self, ctx):
		await ctx.send("group1 test1")

	@commands.group()
	async def group2(self, ctx):
		await ctx.send("group2")

	@group2.command()
	async def test(self, ctx):
		await ctx.send("group2 test2")



def setup(bot):
	bot.add_cog(Test(bot))