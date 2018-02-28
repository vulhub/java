FROM buildpack-deps:bionic-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV JAVA_VERSION="1.8.0_20" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && apt-get update \
    && apt-get install -y unzip \
    && cd /opt \
    && wget http://get.jenv.mvnsearch.org/download/java/java-${JAVA_VERSION}-x64.zip -O /tmp/java.zip \
    && unzip -q /tmp/java.zip -d /opt \
    && mv /opt/java-${JAVA_VERSION} /opt/jdk \
    && apt-get autoremove -y --purge unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/*