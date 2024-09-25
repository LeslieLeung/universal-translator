import os

from dotenv import load_dotenv

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(dotenv_path=project_root)
