import os
from pathlib import Path
from dotenv import load_dotenv
from colorama import Back, Fore, Style

DEBUG = os.getenv("DEBUG", False)

if DEBUG:

    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)
    from settings_files.development import *
    print(f"{Fore.WHITE + Back.YELLOW}We are in DEBUG mode{Style.RESET_ALL}")

else:

    env_path = Path(".") / ".env"
    load_dotenv(dotenv_path=env_path)
    from settings_files.production import *
    print(f"{Fore.WHITE + Back.RED}CAREFUL We are in PRODUCTION mode{Style.RESET_ALL}")
