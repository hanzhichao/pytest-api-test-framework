FROM centos/python-36-centos7
MAINTAINER hzc "superhin@126.com"
#RUN apt-get update -y && \
#apt-get install -y python3-pip python3-dev
#add-apt-repository ppa:deadsnakes/ppa && \
#apt install python3.8


COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip3 install -r requirements.txt
COPY . /
ENTRYPOINT ["python3"]

CMD ["-m", "pytest"]

