# We're using Ubuntu 20.10
FROM biansepang/weebproject:buster

RUN git clone -b Andencento https://github.com/Andencento/Andencento /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot
#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Andencento/Andencento/Andencento/requirements.txt

CMD ["bash", "resource/startup/startup.sh"]
