FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python3-pip python3-dev git gcc g++  dos2unix

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


COPY . /app



RUN dos2unix test/runtests.sh
RUN dos2unix boot.sh && apt-get --purge remove -y dos2unix

RUN chmod +x test/runtests.sh
RUN chmod +x boot.sh

EXPOSE 5000

ENTRYPOINT ["bash"]
