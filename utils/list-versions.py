import io
import sys
import re
import os
import shlex
import requests
import argparse

session = requests.session()
url_pattern = re.compile(r"//download\.oracle\.com/otn/java/jdk/[^']+\.tar\.gz")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}


def main(url, base_dir, version, cookies):
    response = session.get(url, headers=headers)
    for url in url_pattern.findall(response.text):
        filename = url.split('/').pop()
        if 'jdk' not in filename or 'linux-x64' not in filename:
            continue

        output_filename = os.path.join(base_dir, f'{version}', filename).replace('\\', '/')
        if os.path.exists(output_filename) and os.path.getsize(output_filename) > 0:
            continue

        url = f"https:{url}"
        response = session.get(url, headers=headers, allow_redirects=False)
        url = response.headers['Location']
        cookie_headers = dict(**headers, **{'Cookie': cookies})
        response = session.get(url, headers=cookie_headers, allow_redirects=False)
        url = response.headers['Location']

        command = f'''wget -U {shlex.quote(headers['User-Agent'])} -O {shlex.quote(output_filename)} -- {shlex.quote(url)}'''
        print(command)


def parse_cookie_file(f: 'io.TextIOWrapper'):
    data = []
    for line in f.readlines():
        if line.startswith('//'):
            continue

        data.append(line)

    return ''.join(data).replace('\n', '')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A tool that list known Java download urls')
    parser.add_argument('-u', '--url', required=True)
    parser.add_argument('-d', '--dir', required=True, help='Java archive base directory')
    parser.add_argument('--jdk-version', type=int, choices=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15], required=True)
    parser.add_argument('--cookie', required=False)
    parser.add_argument('--cookie-file', type=open, required=False)

    args = parser.parse_args()

    cookies = ''
    if args.cookie:
        cookies = args.cookie
    elif args.cookie_file:
        cookies = parse_cookie_file(args.cookie_file)
    else:
        sys.stdout.write("Cookie is not provided\n")
        sys.stdout.flush()
        parser.print_help()
        sys.exit(1)

    main(args.url, args.dir, args.jdk_version, cookies)
