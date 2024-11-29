FROM python:3.11

WORKDIR /app

# RUN apk update
# RUN apk add --no-cache build-base linux-headers libpq
# RUN apk add --no-cache python-dev
RUN pip install --upgrade pip

RUN pip install --no-cache-dir psycopg2-binary
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src /app/src

EXPOSE 9009

CMD ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "src.app:app"]

