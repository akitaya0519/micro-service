FROM python:3.9
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
RUN apt-get install -y vim less

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN mkdir -p /root/src
COPY requirements.txt /root/src
COPY src/main.py /root/src
WORKDIR /root/src

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip freeze
EXPOSE 80
CMD ["pip", "show","models"]
#CMD ["python", "/root/src/main.py"]