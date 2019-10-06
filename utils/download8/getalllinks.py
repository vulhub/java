import requests
import re
from parse import search


s = requests.session()
s.headers['Cookie'] = r'cookie for www.oracle.com'

response = s.get('https://www.oracle.com/technetwork/java/javase/downloads/java-archive-javase8u211-later-5573849.html')
data = re.findall(br'https://.+?-linux-x64\.tar\.gz', response.content)

print(b'\n'.join(data).decode())
