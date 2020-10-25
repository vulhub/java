#!/usr/bin/env python3
import requests
import os
import re
from constant import *


session = requests.session()
base_dir = os.path.dirname(__file__)
name_pattern = re.compile(r'\-((6|7|8)(u\d+)?)\-')
name9_pattern = re.compile(r'jdk\-((9|10|11|12|13|14|15)([\.\d]+)?)_')


def request_filename(version):
    for filename in session.get('http://api.vulhub.org/download/jdk/%d' % version).json():
        yield filename


def write_dockerfile(version):
    for filename in request_filename(version):
        g1 = name_pattern.search(filename)
        g2 = name9_pattern.search(filename)
        if g1:
            g = g1
        elif g2:
            g = g2
        else:
            continue

        template = globals()['DOCKERFILE_TEMPLATE_%d' % version]
        dockerfile = os.path.join(base_dir, 'jdk', '%d' % version, g.group(1), 'Dockerfile')
        os.makedirs(os.path.dirname(dockerfile), mode=0o755, exist_ok=True)

        with open(dockerfile, 'w', encoding='utf-8') as f:
            f.write(template % filename)


def main():
    for version in (6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
        write_dockerfile(version)


if __name__ == '__main__':
    main()
