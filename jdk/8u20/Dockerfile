FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV JAVA_VERSION="1.8.0_20" JAVA_HOME="/opt/jdk"

ADD http://get.jenv.mvnsearch.org/download/java/java-${JAVA_VERSION}-x64.zip /tmp/java.zip

RUN set -ex \
    && apt-get update \
    && apt-get install -y unzip \
    && unzip -q /tmp/java.zip -d /opt \
    && mv /opt/java-${JAVA_VERSION} /opt/jdk \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100 \
    && apt-get autoremove -y --purge unzip \
    && rm -rf /var/lib/apt/lists/* /tmp/*