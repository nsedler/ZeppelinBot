import discord
import os

from discord.ext import commands

INITIAL_EXTENSIONS = {
	'cogs.echo',
	'cogs.info',
	'cogs.owner',
	'cogs.liveYTSubs'
}


def get_prefix(bot, message):


	prefixes = ['$', '%', '.']
	if not message.guild: return '?'

	return commands.when_mentioned_or(*prefixes)(bot, message)


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
		total_guilds = len(self.guilds)
		await self.change_presence(activity=discord.Game("Currently helping " + str(total_guilds) + " guilds"))

	async def on_message(self, message):

		if message.author.bot:
			return
		await self.process_commands(message)

	def run(self):
		super().run(self.token)


if __name__ == '__main__':
	zepbot = ZeppelinBot()
	zepbot.run()