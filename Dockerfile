FROM python:3.13.1

# Создаем рабочую директорию внутри контейнера
WORKDIR .

# Копируем файлы проекта в рабочую директорию
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда запуска
CMD ["python", "bot/main.py"]