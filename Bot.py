import os
from dotenv import load_dotenv
import openai
import discord
from discord.ext import commands

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

openai.api_key = OPENAI_API_KEY
bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content_list = []
    if message.content:
        content_list.append(message.content)

    for attachment in message.attachments:
        content_list.append({"image": await attachment.read()})

    content = " ".join([str(item) for item in content_list])

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": content}
        ]
    )

    assistant_response = completion.choices[0].message["content"]
    await message.channel.send(assistant_response)

bot.run(DISCORD_TOKEN)