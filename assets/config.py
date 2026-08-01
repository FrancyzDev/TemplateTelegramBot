import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / 'config.json', encoding="utf-8") as f:
    config_data = json.load(f)

BOT = config_data.get("BOT") # БОТ
BOT_TOKEN = BOT.get("TOKEN") # Токен бота
BOT_ADMIN_IDS = BOT.get("ADMIN_IDS") # Id админов
BOT_MUST_HAVE_CHANNELS = BOT.get("MUST_HAVE_CHANNELS") # ID - ссылка | Каналов необходимых для использования бота

DATABASE = config_data.get("DATABASE") # База данных
DATABASE_PATH = DATABASE.get("PATH") # Connection string к бд
