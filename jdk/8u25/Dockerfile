FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV JAVA_VERSION="8u25" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- https://vulhub.sgp1.digitaloceanspaces.com/jdk/java8/jdk-${JAVA_VERSION}-linux-x64.tar.gz | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java ${JAVA_HOME}/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac ${JAVA_HOME}/bin/javac 100

WORKDIR ${JAVA_HOME}