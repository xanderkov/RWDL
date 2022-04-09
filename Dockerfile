FROM python:3.10.2

COPY ./requirements.txt /root/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r /root/requirements.txt

WORKDIR /root/docker

COPY . /root/docker

CMD ["python", "src/bot.py"] 
