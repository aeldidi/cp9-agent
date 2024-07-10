import tomllib

import discord

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged on as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        if message.author.id == 1259617744379183124:
            await message.delete()
            msg = discord.Embed(
                color=discord.Color.from_rgb(235, 64, 52),
                title="SUNDANCE MESSAGE DETECTED: BUSTER CALL INITIATED",
            )
            msg.set_image("https://tenor.com/view/buster-call-ohara-gif-27694097")
            await message.channel.send(embed=msg)
    except Exception as e:
        print(f"exception: {e}")


client.run(config["token"])
