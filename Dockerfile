FROM python:3.12-slim

WORKDIR /app

RUN pip install lerobot==0.5.1

COPY . .

CMD ["python", "scripts/train.py"]
