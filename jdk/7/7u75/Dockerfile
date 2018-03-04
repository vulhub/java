FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="jdk-7u75-linux-x64.tar.gz" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/7/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
