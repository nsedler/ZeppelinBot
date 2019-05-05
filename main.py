import discord
import os
import json

from discord.ext import commands

INITIAL_EXTENSIONS = {
	'cogs.info',
	'cogs.owner',
	'cogs.fun',
	'cogs.preferences',
	'cogs.test'
}



def get_prefix(bot, message):

	with open("prefixes.json") as f:
		prefixes = json.load(f)

	id = str(message.guild.id)

	if id in prefixes:
		return prefixes.get(id)
	else:
		return '$'



class ZeppelinBot(commands.Bot):

	def __init__(self):
		super().__init__(command_prefix=get_prefix, description="Led Zeppelin rules, man!")
		self.owner_id = 185063150557593600
		self.token = os.getenv("TOKEN")

		for extension in INITIAL_EXTENSIONS:
			try:
				self.load_extension(extension)
				print("Successfully loaded: " + extension)
			except Exception as e:
				print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

	async def on_ready(self):
		print("Logged in as: ")
		print("Username: " + self.user.name)
		print("ID: " + str(self.user.id))

		total_users = len(set(self.get_all_members()))

		await self.change_presence(activity=discord.Game("Currently helping " + str(total_users) + " users, man!"))

	async def on_message(self, message):

		if message.author.bot:
			return
		await self.process_commands(message)

	def run(self):
		super().run(self.token)

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		print(error)


if __name__ == '__main__':
	zepbot = ZeppelinBot()
	zepbot.run()
