from pydantic_settings import BaseSettings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

class Config(BaseSettings):

    TELEGRAM_TOKEN: str

    DB_URL: str

    WORKGROUP_CHAT_ID : str

    WEATHER_API_KEY : str

    CURRENT_CITY : str
    
    class Config:
        env_file = f"{BASE_DIR}/.env"

       
config = Config()

mainmenu_path = f"{BASE_DIR}/txt/mainmenu.txt"

start_path = f"{BASE_DIR}/txt/start.txt"





