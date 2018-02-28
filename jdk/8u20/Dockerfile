FROM buildpack-deps:bionic-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV JAVA_VERSION "1.8.0_20"

RUN set -ex \
    && apt-get update \
    && apt-get install -y unzip \
    && curl -L -s get.jenv.io | bash \
    && source /root/.jenv/bin/jenv-init.sh \
    && jenv install java ${JAVA_VERSION} \
    && apt-get autoremove -y --purge unzip \
    && rm -rf /var/lib/apt/lists/*