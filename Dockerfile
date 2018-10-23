FROM python:3

RUN apt-get update && apt-get install -y vim && apt-get clean

WORKDIR /usr/npuzzle

COPY author ./
COPY README.md ./
COPY requirements.txt ./
COPY src ./src/
COPY test ./test/
COPY setup.py ./

RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install .

ENTRYPOINT /bin/bash