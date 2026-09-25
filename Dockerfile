FROM python:3.12-alpine
WORKDIR /app
COPY ./app/server.py .
CMD ["python", "server.py"]