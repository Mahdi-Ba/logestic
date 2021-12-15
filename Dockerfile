FROM python:3.7.10
RUN apt update && \
apt install -y sudo python3-dev libpq-dev gettext
RUN pip install psycopg2
WORKDIR /tboof
COPY . /tboof/
RUN pip3 install -r requirements.txt