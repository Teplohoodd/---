import discord
import requests
from discord.ext import commands
from bs4 import BeautifulSoup
import random
import nltk

nltk.download('punkt')

intents = discord.Intents.default()
intents.message_content = True

config = {
    'token': 'Your Token here',
    'prefix': '/'
}
random_page_one = random.randint(1, 4138)
bot = commands.Bot(command_prefix=config['prefix'], intents=intents)

@bot.command()
async def fact(ctx):
    random_page = random.randint(1, 4138)
    url = f"http://facts.museum/{random_page}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    fact_blocks = soup.find_all(class_="content")
    
    if fact_blocks:
        random_fact_block = random.choice(fact_blocks)
        random_fact = random_fact_block.text.strip()
        print(random_fact)
        first_sentence = nltk.sent_tokenize(random_fact)[0]
        image_url = f"http://facts.museum/img/facts/{random_page}.jpg"
        
        embed = discord.Embed(title=first_sentence, description=random_fact)
        embed.set_image(url=image_url)
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Факты не найдены.")
@bot.command()
async def day_fact(ctx):
    
    url = f"http://facts.museum/{random_page_one}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    fact_blocks = soup.find_all(class_="content")
    
    if fact_blocks:
        random_fact_block = random.choice(fact_blocks)
        random_fact = random_fact_block.text.strip()
        first_sentence = nltk.sent_tokenize(random_fact)[0]
        image_url = f"http://facts.museum/img/facts/{random_page_one}.jpg"
        
        embed = discord.Embed(title=first_sentence, description=random_fact)
        embed.set_image(url=image_url)
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Факты не найдены.")
bot.run(config["token"])
