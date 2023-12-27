from dis import disco
from sys import executable
from turtle import title
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='+', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Le bot D-Shop est bien démarer !")

excluded_members = []

@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    embed = discord.Embed(title="Clear", description="Salon clear avec succès !", color = 0xab99d7)
    await ctx.send(embed=embed)

@bot.command()
async def lock(ctx):
    channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=True)
    embed = discord.Embed(title="Lock", description="Salon Lock 🔒", color= 0xff2400)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1166826512457154623/1173027906721689610/05-09-53-216_512.png?ex=6562765e&is=6550015e&hm=a4efa66631d0285d89e8007badb42ed8ceaeb3b50c1fe058aed9a13477b5c4f6&")
    await ctx.send(embed=embed)

@bot.command()
async def unlock(ctx):
    channel = ctx.channel
    await channel.set_permissions(ctx.guild.default_role, send_messages=True, read_messages=True)
    embed = discord.Embed(title="Unlock", description="Salon Unlock 🔓", color = 0xff2400)
    embed.set_image(url="https://cdn.pixabay.com/animation/2022/07/31/05/09/05-09-53-216_512.gif")
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def botpresence(ctx):
    await bot.change_presence(activity=discord.Streaming(name='+help', url = 'https://discord.com'))
    embed = discord.Embed(title="RishPresence", description=f"Le RishPresence du bot a bien été changé ! 🟣", color = 0x7640ff)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def ticket_spawn(ctx):
    # Créer le message initial avec le bouton
    embed = discord.Embed(title="🎓・you're Ticket", description="Cliquez sur la réaction pour créer un nouveau de ticket en cas d'aides, achats...")
    message = await ctx.send(embed=embed)

    # Ajouter le bouton sous forme de réaction au message
    await message.add_reaction("😁")

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    # Vérifier que la réaction est bien 💎
    if str(reaction.emoji) == "😁":
        # Vérifier que la réaction a été ajoutée à un message du bot
        if isinstance(reaction.message.channel, discord.DMChannel):
            return

        # Créer le salon de ticket
        ticket_name = f"ticket-{user.name}"
        overwrites = {
            reaction.message.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            reaction.message.guild.me: discord.PermissionOverwrite(read_messages=True),
            user: discord.PermissionOverwrite(read_messages=True)
        }
        ticket_channel = await reaction.message.guild.create_text_channel(name=ticket_name, overwrites=overwrites)
        await ticket_channel.send(f"Bienvenue dans votre ticket, {user.mention} !")

@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)

if __name__ == "__main__":
    bot.run("TOKEN")
