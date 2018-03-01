FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV JAVA_VERSION="8u25" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && wget https://vulhub.sgp1.digitaloceanspaces.com/jdk/java8/jdk-${JAVA_VERSION}-linux-x64.tar.gz

RUN set -ex \
    && apt-get update \
    && apt-get install -y unzip \
    && unzip -q /tmp/java.zip -d /opt \
    && mv /opt/jdk-${JAVA_VERSION}-linux-x64 /opt/jdk \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100 \
    && apt-get autoremove -y --purge unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/*