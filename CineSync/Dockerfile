FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "CineSync.wsgi:application"]
