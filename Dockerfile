# Базовый образ Python
FROM python:3.12

# Устанавливаем зависимости системы
RUN apt-get update && apt-get install -y \
    libpq-dev gcc netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*


# Создаём рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y gettext

# Указываем переменную окружения
ENV PYTHONUNBUFFERED=1

RUN chmod +x /app/entrypoint.sh

# Запускаем контейнер через этот скрипт
ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main.wsgi:application"]
