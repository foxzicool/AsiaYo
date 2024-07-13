
FROM python:3.8-slim

WORKDIR /app

RUN pip install --no-cache-dir flask flask_cors alpha_vantage
RUN apt-get update && apt-get install -y curl
RUN pip install --no-cache-dir flask flask_cors alpha_vantage pydantic

COPY . /app

EXPOSE 5000

ENV NAME World

CMD ["python", "面試.py"]

