# Using Python Slim-Buster
FROM xluxz/geezproject:buster
# Andencento By Noob Stranger
#yaudah iya

RUN git clone -b https://github.com/Team-Andencento/Andencento /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]
