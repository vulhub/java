DOCKERFILE_TEMPLATE_15 = r'''FROM buildpack-deps:buster-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/15/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_14 = r'''FROM buildpack-deps:buster-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/14/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_13 = r'''FROM buildpack-deps:buster-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/13/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_12 = r'''FROM buildpack-deps:buster-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/12/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_11 = r'''FROM buildpack-deps:buster-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/11/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_10 = r'''FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/10/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_9 = r'''FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/9/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_8 = r'''FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/8/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_7 = r'''FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

RUN set -ex \
    && mkdir -p ${JAVA_HOME} \
    && cd ${JAVA_HOME} \
    && wget -qO- http://api.vulhub.org/download/jdk/7/${FILENAME} | tar xz --strip-components=1 \
    && update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 100 \
    && update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 100

WORKDIR ${JAVA_HOME}
'''

DOCKERFILE_TEMPLATE_6 = r'''FROM buildpack-deps:stretch-curl

LABEL maintainer="phithon <root@leavesongs.com>"

ENV FILENAME="%s" JAVA_HOME="/opt/jdk"

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
'''