import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import json

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

with open("creds.json", "r") as creds:
    data = json.load(creds)["creds"]
    token = data["bot_token"]

@client.event
async def on_ready():
    print('The Jambot is here. Hello.')
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Watching over skids'))

@client.event
async def on_member_join(self, member):
    channel = discord.utils.get(message.guild.channels, name='general')
    await channel.send(f'{member} has joined the server. :smile:')

@client.event
async def on_member_remove(self, member):
    channel = discord.utils.get(message.guild.channels, name='general')
    await channel.send(f'{member} has left the server. :pensive:')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('Please give all the arguments.')
    elif isinstance(error,commands.errors.BadArgument):
        await ctx.send("Conversion of arguments failed.")
    print(f"ERROR: {error}")

# @client.command(brief = 'Reloads cog.', description = 'Do ";reload cog".')
# @has_permissions(administrator = True)
# async def reload(ctx, extension):
#     if ctx.message.author.id == 448519423901433876:
#         client.unload_extension(f'cogs.{extension}')
#         client.load_extension(f'cogs.{extension}')
#     else:
#         await ctx.send("You must be Jammy.")
#         return

#     await ctx.send(f'Successfully reloaded "{extension}".')

#bot hosted on heroku command not needed

client.load_extension('cogs.fun')
client.load_extension('cogs.admin')
client.load_extension('cogs.useful')
client.load_extension('cogs.reddit')
client.load_extension('cogs.maths')
client.run(token)#api key here :)
