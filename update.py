#!/usr/bin/env python3
import requests
import os
import re

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
session = requests.session()
base_dir = os.path.dirname(__file__)
name_pattern = re.compile(r'\-((6|7|8)(u\d+)?)\-')
name9_pattern = re.compile(r'jdk\-((9|10)([\.\d]+)?)_')


def request_filename(version):
    for filename in session.get('http://api.vulhub.org/download/jdk/%d' % version).json():
        yield filename


def write_dockerfile(version):
    for filename in request_filename(version):
        g1 = name_pattern.search(filename)
        g2 = name9_pattern.search(filename)
        if g1: g = g1
        elif g2: g = g2
        else: continue

        template = globals()['DOCKERFILE_TEMPLATE_%d' % version]
        dockerfile = os.path.join(base_dir, 'jdk', '%d' % version, g.group(1), 'Dockerfile')
        os.makedirs(os.path.dirname(dockerfile), mode=0o755, exist_ok=True)

        with open(dockerfile, 'w', encoding='utf-8') as f:
            f.write(template % filename)


def main():
    for version in (6, 7, 8, 9, 10):
        write_dockerfile(version)


if __name__ == '__main__':
    main()
