import discord #Il faut au préalable avoir installé le package python, pour le faire, ouvrez cmd ou votre terminal puis entrez la ligne suivante : pip install discord
from discord.ext import commands #Nécessaire pour importer les commandes

bot = commands.Bot(command_prefix="VotrePréfixeICI") #Définit "bot". N'oubliez pas de modifier avec le préfixe voulu

@bot.event
async def on_ready():
    print("I'm alive")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run("YourTokenHere") # N'oubliez pas d'insérer votre token ici, sans quoi le script ne fonctionnera pas.
