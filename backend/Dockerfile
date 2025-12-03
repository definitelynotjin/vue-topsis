FROM python:3.13-alpine3.22

WORKDIR /app

COPY requirements.txt .
RUN python3 -m venv /app/venv \
  && /app/venv/bin/pip install --upgrade pip \
  && /app/venv/bin/pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["/app/venv/bin/python", "app.py"]
