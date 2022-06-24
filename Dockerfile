FROM centos:7

RUN yum update -y && yum install -y rpm-build
#RUN yum update -y

WORKDIR /app

ENTRYPOINT ["/bin/sh", "-c", "while :; do sleep 10; done"]
