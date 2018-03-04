FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="jdk-6u33-linux-x64.bin" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -q -O jdk.bin http://api.vulhub.org/download/jdk/6/${FILENAME} \
    && chmod +x jdk.bin \
    && yes | ./jdk.bin \
    && rm -rf jdk.bin \
    && mv jdk1.6.0_*/* ./ \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
