import discord

from discord.ext import commands


class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(hidden=True)
	@commands.is_owner()
	async def test(self, ctx):
		e = discord.Embed()
		e.set_image(url="https://purr.objects-us-east-1.dream.io/i/20170122_215212.jpg")
		await ctx.send(embed=e)



def setup(bot):
	bot.add_cog(Test(bot))