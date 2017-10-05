FROM ubuntu:16.04

MAINTAINER alberto.rincon@beeva.com

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y build-essential \
                       gcc-4.9 \
                       g++-4.9 \
                       cmake \
                       make \
                       libbz2-dev \
                       libdb++-dev \
                       libdb-dev \
                       libssl-dev \
                       openssl \
                       libreadline-dev \
                       autoconf \
                       libtool \
                       git \
                       autotools-dev \
                       libbz2-dev \
                       libicu-dev \
                       libboost-all-dev \
                       python \
                       python-dev \
                       python-pip\
                       wget \
                       python-tk \
                       python-opencv \
                       libgtk2.0-dev

RUN rm -rf /var/lib/apt/lists/*

RUN wget http://dl.bintray.com/boostorg/release/1.65.0/source/boost_1_65_0.tar.gz \
    && tar -xzf boost_1_65_0.tar.gz \
    && cd boost_1_65_0/ \
    && ./bootstrap.sh --prefix=/opt/boost_1_65_0 --with-libraries=python  \
    && ./b2 \
    && ./b2 install

RUN pip install face_recognition jupyter notebook google-cloud matplotlib scikit-image

RUN mkdir -p -m 700 /root/.jupyter/ && echo "c.NotebookApp.ip = '*'" >> /root/.jupyter/jupyter_notebook_config.py

RUN git clone https://github.com/beeva-albertorincon/beeva-poc-google-ocr-faces.git \
    && cd beeva-poc-google-ocr-faces \

EXPOSE 8888

ENTRYPOINT '/bin/bash' 
