# Import main modules
import discord

# Import secondary modules
from discord import app_commands
from discord.ext import commands


class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Delete specified number of messages from current channel
    @commands.command(name='clear', help='Comando habilitado apenas para Admins!\n\nUso: %clear numDeMsgs (entre 1 e 100)\n\nO comando deve ser executado dentro do canal que deseja limpar\n\nComando habilitado apenas para Admins!')
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amt: int):

        await ctx.channel.purge(limit=amt)

        embed = discord.Embed(
            title=f'{amt} Mensagens apagadas',
            description=f'**{amt}** Mensagens apagadas com **SUCESSO**'
            )
        embed.add_field(name='Solicitado por ', value=ctx.author.name)
        embed.set_footer(text='essa mensagem se auto-apagará em 5 segundos')

        msg = await ctx.send(embed=embed)

        await msg.delete(delay=5)

async def setup(bot):
    await bot.add_cog(Mod(bot))