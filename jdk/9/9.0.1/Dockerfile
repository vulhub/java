FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="jdk-9.0.1_linux-x64_bin.tar.gz" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/9/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
