import discord
from discord.ext import commands

class admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    #EVENTS

    @commands.Cog.listener() #check if this works instead of going off of ur old code jamie
    async def on_ready(self):
        print('The Jambot is here. Hello.')
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('Watching over skids'))

    @commands.Cog.listener()
    async def on_member_join(self, member): #also check if this works lol- will run one big test at the end probably
        channel = discord.utils.get(message.guild.channels, name='general')
        await channel.send(f'{member} has joined the server.')

    @commands.Cog.listener()
    async def on_member_remove(self, member): #should probably stop putting a note to check at every function lmao
        channel = discord.utils.get(message.guild.channels, name='general')
        await channel.send(f'{member} has left the server.')
    
    @commands.Cog.listener()
    async def on_commmand_error(self, ctx, error): 
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please give all the arguments.')
        print(f"ERROR: {error}")

    #ACTUAL ADMIN STUFF (im not screaming, my eyesight is just poor so it helps me see)

    @commmands.command(brief='Clear messages in channel (default 5).', description='Do ".byebye amount_to_clear".')
    @commands.has_permissions(administrator=True)
    async def byebye(self, ctx, amount=6): #6 because it needs to clear the command message too
    await ctx.channel.purge(limit=amount+1)

    @commands.command(brief='Kicks users.', description='Do ".kick @user".')
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
    user = await commands.get_user_info(member.ID) #not 100% sure this works
    await member.kick(reason=reason)
    await commands.send_message(user, "Damn, I'm just a lowly bot but even I think you should have been kicked :/")

def setup(client):
    client.add_cog(admin(client))