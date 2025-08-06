FROM python:3.11-slim-buster

LABEL maintainer="Scott Gibb"

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential=12.9 python3-pip=20.3.4-4+deb11u1 && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . . 
COPY python-requirements.txt ./python-requirements.txt
RUN pip3 install --no-cache-dir -r python-requirements.txt

ENTRYPOINT ["python3"]
CMD ["-u","src/Main.py"]