import os
from pathlib import Path
import environ

# choosen HERE environment
env_name = os.getenv("DJANGO_ENV", "dev")

# choosen environment file
env_file = ".env.dev" if env_name == "dev" else ".env.prod"

# loading file before importing settings
env = environ.Env()
environ.Env.read_env(Path(__file__).resolve().parent.parent.parent / env_file)

# import settings based on the environment
if env_name == "prod":
    from .prod import *
else:
    from .dev import *
