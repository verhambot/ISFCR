FROM python:3

RUN \
  apt-get update && \
  apt-get install -y socat && \
  useradd -m ctf

WORKDIR /home/ctf

COPY . .

RUN \
    chown -R root:root /home/ctf && \
    chmod -R 555 /home/ctf

USER ctf
CMD [ "socat", "TCP-LISTEN:1337,reuseaddr,fork", "EXEC:'python3 app.py'" ]
EXPOSE 1337
