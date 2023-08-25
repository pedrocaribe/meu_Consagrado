# Import main modules
import random, discord, aiohttp, praw, asyncpraw

# Import secondary modules
from discord.ext import commands
from settings import REDDIT_APP_ID, REDDIT_APP_SECRET, REDDIT_SAFE_MEME_SUBREDDITS
from discord import app_commands


# Define class
class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = None
        if REDDIT_APP_SECRET and REDDIT_APP_ID:
            self.reddit = asyncpraw.Reddit(client_id=REDDIT_APP_ID, client_secret=REDDIT_APP_SECRET, user_agent=f'DISCORD_BOT:{REDDIT_APP_ID}:1.0')

        '''Commands defined in this cog are for the entertainment and use with images.

        images v1.00'''

    # Command to retrieve images/gifs from reddit
    @app_commands.command(name='reddit', description='Busca imagens do Reddit')
    async def reddit(self, interaction: discord.Interaction, *, subreddit: str = ""):

        # Check if reddit ID and SECRET are functional
        if self.reddit:

            # Check if command was ran from +18 channel, if yes, deliver requested image from subreddit to user.
            if interaction.channel.is_nsfw():
                
                # Retrieve pool of submissions
                if " " in subreddit:
                    subreddit = subreddit.replace(' ', '+')

                submissions = await self.reddit.subreddit(subreddit)
                pool = submissions.top(
                    limit=50, 
                    time_filter='day'
                )

                # Send random post from top 50 submissions of the day
                to_send = random.choice([submission async for submission in pool])
                return await interaction.response.send_message(to_send.url)


            # If command was not ran from +18 channel, consider only list of safe subreddits, and default to 'funny'.
            chosen_subreddit = REDDIT_SAFE_MEME_SUBREDDITS[0]

            # If subreddit was specified by user, check if it's in list of safe subreddits.
            if subreddit:
                if subreddit in REDDIT_SAFE_MEME_SUBREDDITS:
                    chosen_subreddit = subreddit

                # If specified subreddit is not present, return instructions to user.
                else:
                    return await interaction.response.send_message(f"Por favor selecione um subreddit da lista a seguir: **{', '.join(REDDIT_SAFE_MEME_SUBREDDITS)}**.\nPara subreddits 🔞, solicite acesso à area para um Admin.")
            
            # Retrieve pool of submissions
            submissions = await self.reddit.subreddit(chosen_subreddit)

            submissions = submissions.top(
                limit=50, 
                time_filter='all'
            )

            # Send random post from top 50 submissions of the day
            to_send = random.choice([submission async for submission in submissions])
            return await interaction.response.send_message(to_send.url)

        # If credentials are invalid, contact Admin
        else:
            return await interaction.response.send_message("Erro no comando, contate um Admin")


    # Command to retrieve random cat image
    @app_commands.command(name='gato', description='Imagem aleatória de um gato')
    async def cat(self, interaction: discord.Interaction):

        # API Request
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://cataas.com/cat?json=true") as r:
                data = await r.json()

                embed = discord.Embed(
                    title="Meow"
                )

                embed.set_image(url=f"https://cataas.com/{data['url']}")
                embed.set_footer(text='https://cataas.com/')

                await interaction.response.send_message(embed=embed)


    # Command to retrieve random dog image
    @app_commands.command(name='cachorro', description='Imagem aleatória de um cachorro')
    async def dog(self, interaction: discord.Interaction):

        # API Request
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                data = await r.json()

                embed = discord.Embed(
                    title="Woof"
                )
                
                embed.set_image(url=data['message'])
                embed.set_footer(text='https://dog.ceo/')

                await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Images(bot))