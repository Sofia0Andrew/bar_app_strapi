from dotenv import load_dotenv
import os

load_dotenv()

#оставила свои данные в значениях по умолчанию, если в .env записать свои значения, то будут использоваться
# указанные в .env значения переменных окружения
SECRET_KEY = os.getenv("SECRET_KEY", "1234")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "1234567")
DATABASE_HOST = os.getenv("DATABASE_HOST", "127.0.0.1")
DATABASE_NAME = os.getenv("DATABASE_NAME", "bar_app")