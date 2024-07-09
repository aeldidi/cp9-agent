import tomllib

import discord

with open("config.toml", "r") as f:
    config = tomllib.load(f)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        try:
            if message.author.id == 1259617744379183124:
                await message.delete()
                msg = discord.Embed(
                    color=(235, 64, 52),
                    title="SUNDANCE MESSAGE DETECTED: BUSTER CALL INITIATED",
                )
                msg.set_image("https://tenor.com/view/buster-call-ohara-gif-27694097")
                await message.channel.send(embed=msg)
        except Exception as e:
            print(f"exception: {e}")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config["token"])
