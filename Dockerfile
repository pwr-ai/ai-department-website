FROM ubuntu:latest
WORKDIR /app
RUN apt-get update
RUN apt-get install -y golang-go
RUN apt-get install -y git
RUN apt-get install -y nodejs

ENTRYPOINT ["./hugo", "server"]
