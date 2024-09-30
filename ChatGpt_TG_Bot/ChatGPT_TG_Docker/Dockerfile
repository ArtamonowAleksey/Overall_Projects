# Используем официальный образ Python с сокращенной версией
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

# Копируем содержимое текущего каталога в рабочую директорию контейнера
COPY . /app

# Указываем команду, которая будет выполнена при запуске контейнера
CMD ["python", "GPTbotClean.py"]