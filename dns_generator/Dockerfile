FROM python:3.9-slim

WORKDIR /app

COPY 3rd_lev_domains.csv /app/3rd_lev_domains.csv
COPY generator.py /app/generator.py

RUN apt-get update && apt-get install -y dnsutils

CMD ["python", "generator.py"]
