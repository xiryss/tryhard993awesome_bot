FROM python:3.9-alpine
RUN pip install aiogram

WORKDIR /app
COPY main.py .

CMD ["python3", "main.py"]