import requests
import re
from parse import search


s = requests.session()
s.headers['Cookie'] = r'cookie for www.oracle.com'

response = s.get('https://www.oracle.com/java/technologies/java-archive-javase10-downloads.html')
data = re.findall(br'//.+?linux-x64_bin\.tar\.gz', response.content)

print(b'\n'.join(data).decode())
