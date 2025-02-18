#!/bin/sh

echo "Ждём, пока база данных запустится..."
while ! nc -z db 5432; do sleep 1; done
echo "База данных запущена."

# Выполняем миграции
python manage.py migrate

# Собираем статику
python manage.py collectstatic --noinput

# Запускаем сервер
exec "$@"
