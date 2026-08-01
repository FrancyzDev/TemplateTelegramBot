import json
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "i18n.json", encoding="utf-8") as f:
    config_data = json.load(f)

LANGUAGES = {
    "us": {
        "flag": "🇺🇸",
        "text": "Select language"
    },
    "ua": {
        "flag": "🇺🇦",
        "text": "Обрати мову"
    },
    "ru": {
        "flag": "🇷🇺",
        "text": "Выбрать язык"
    },
}

LANGUAGES_SELECT_TEXT = '\n\n'.join([f"{val.get('flag')} {val.get('text')}" for key, val in LANGUAGES.items()])
LANGUAGES_SELECT_BUTTONS = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=val.get('flag'), callback_data=f"language|{key}") for key, val in LANGUAGES.items()]])
TEXTS = config_data

def get_text(key: str, lang: str, **kwargs) -> str:
    text = TEXTS.get(key, f"[MISSING: {key}]")
    lang_text = text.get(lang, f"[MISSING: {lang}]")
    if kwargs:
        try:
            lang_text = lang_text.format(**kwargs)
        except KeyError as e:
            print(f"⚠️ Missing parameter {e} for key {key}")
    return lang_text