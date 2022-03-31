FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV ENV=PROD

ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "server:app"]
