FROM ubuntu:latest

RUN \
  useradd -m ctf && \
  apt-get update && \
  apt-get install -y gcc

WORKDIR /home/ctf

COPY . .

RUN \
  chown -R root:root /home/ctf && \
  chmod -R 555 /home/ctf && \
  ./compile.sh

USER ctf
CMD ./ynetd -p 1337 ./segfault
EXPOSE 1337
