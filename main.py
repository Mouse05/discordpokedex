#importing Discord.py
import discord
import requests
import pypokedex
from discord.ext import commands

#gets client object from discord
bot = commands.Bot(command_prefix='!')

#pokemon code (hopefully?)
def pokemon_name_generator(p):
    pokemon = pypokedex.get(name = str(p))
    return ("Your pokemon's dex number is: " + str(pokemon.dex) + 
        ". \nYour pokemon's name is: " + str(pokemon.name.upper()) + 
        ". \nYour pokemon's abilities are: " + str(pokemon.abilities) + 
        ". \nYour pokemon's types are: " + str(pokemon.types) + 
        ". \nYour pokemon's sprite is: " + str(pokemon.sprites.front.get("default")))

@bot.command()
async def pokemon(ctx, pokemon_name):
    await ctx.reply(pokemon_name_generator(pokemon_name))
