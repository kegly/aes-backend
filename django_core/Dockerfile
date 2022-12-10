# получаем image для нашего питона
FROM python:3.11

# устанавливаем рабочую директорию
WORKDIR /django_core

# задаём переменные окружения, чтобы
# предотвратить ряд событий, а именно:
# создания .pyc файлов и использования
# питоном буффера для stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# ставим зависимости
RUN pip install --upgrade pip
COPY requirements .
RUN pip install -r production.txt

# копируем проект
COPY . .