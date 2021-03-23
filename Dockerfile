FROM python:3.9.2-buster

RUN apt-get update && apt install python3-pip -y

COPY app /app

ADD hhttps://raw.githubusercontent.com/insidus341/valheim-bot/master/app/server_stats.py /app/server_stats.py

WORKDIR /app

RUN pip3 install -r requirements.txt 

CMD ["app.py"]

ENTRYPOINT ["python3"]
