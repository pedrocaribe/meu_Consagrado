import os
import sqlite3
from itertools import cycle
from discord.ext import commands

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, "data")

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", False)
GUILD_DB = os.getenv("GUILD_DB", False)
MSG_DB = os.getenv("MSG_DB", False)
STUDY_DB = os.getenv("STUDY_DB", False)
TICKET_DB = os.getenv("TICKET_DB", False)
CHATGPT_API_TOKEN = os.getenv("CHATGPT_API_TOKEN", False)

# Reddit configuration
REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)
REDDIT_SAFE_MEME_SUBREDDITS = [
    'funny',
    'meme',
    'memes',
    'wtf',
    'engraçado'
]

# Spotify configuration
SPOTIFY_CID = os.getenv("SPOTIFY_CID", False)
SPOTIFY_SECRET = os.getenv("SPOTIFY_SECRET", False)

# MISC
IGNORE_ERRORS = ()

FRASE_MEIO = [
            'meu Magnata',
            'meu Feiticeiro',
            'meu Imperador',
            'meu Diplomata',
            'meu Embaixador',
            'meu Almirante',
            'meu Comendador',
            'meu Engenheiro',
            'meu Bacharel',
            'meu Chanceler',
            'meu Eclesiasta',
            'meu Paladino',
            'meu Estivador',
            'meu Menestrel',
            'meu Comensal',
            'meu Suserano',
            'meu Leviatã',
            'meu Kylo Ren',
            'meu Cangaceiro',
            'meu Sambarilove',
            'meu Dig Dig Joy',
            'meu Aliado',
            'meu Querido',
            'meu Parceiro',
            'meu Aliado',
            'meu Bom',
            'meu Rei',
            'meu Amigo',
            'meu Doutrinador',
            'meu Queridão',
            'gente boa',
            'meu Mestre',
            'Fera',
            'meu Patrão',
            'Chapa',
            'meu Chapa',
            'Chefia',
            'Campeão'
            ]

STATUS = cycle([
                'Feito em Python',
                'Coded in Python',
                'By Pedro Caribé',
                'Pythonic Way',
                'Sugestões?',
                'Suggestions?',
                'Dúvidas? %help'
                ])
