import discord

from discord.ext import commands


INITIAL_EXTENSIONS = {
	'cogs.echo',
	'cogs.ping'
}


class ZeppelinBot(commands.Bot):

	def __init__(self):
		super().__init__(command_prefix='.', description="Led Zeppelin rules, man!")
		self.owner_id = 185063150557593600
		self.token = "NTY5OTkxMDQ2NDI4MDk4NjM3.XL4rjA.6ek0zfaTBjGeNnome-NMk7OFeWg"

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

	async def on_message(self, message):
		if message.author.bot:
			return
		await self.process_commands(message)

		print("=============")
		print("New Message:")
		print(message.author.name + " said:")
		print(message.content)
		print("=============")

	def run(self):
		super().run(self.token)


if __name__ == '__main__':
	zepbot = ZeppelinBot()
	zepbot.run()
