import os
import requests
import subprocess
from parse import search


headers1 = {"Cookie": r'''cookie for download.oracle.com'''}
headers2 = {"Cookie": r'''cookie for edelivery.oracle.com'''}
data = r'''https://download.oracle.com/otn/java/jdk/8u212-b10/59066701cf1a433da9770636fbc4c9aa/jdk-8u212-linux-x64.tar.gz
https://download.oracle.com/otn/java/jdk/8u212-b10/59066701cf1a433da9770636fbc4c9aa/jre-8u212-linux-x64.tar.gz
https://download.oracle.com/otn/java/jdk/8u212-b10/59066701cf1a433da9770636fbc4c9aa/server-jre-8u212-linux-x64.tar.gz
https://download.oracle.com/otn/java/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jdk-8u211-linux-x64.tar.gz
https://download.oracle.com/otn/java/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/jre-8u211-linux-x64.tar.gz
https://download.oracle.com/otn/java/jdk/8u211-b12/478a62b7d4e34b78b671c754eaaf38ab/server-jre-8u211-linux-x64.tar.gz
'''


for link in data.split('\n'):
    link = link.strip()
    if not search('jdk-{}-linux-x64.tar.gz', link):
        continue
        
    r = search('https://download.oracle.com/otn/java/jdk/8u{:d}', link)
    if r is None:
        continue
        
    if r[0] <= 172:
        continue
    
    response = requests.head(link, allow_redirects=False, headers=headers1)
    if not (300 <= response.status_code < 400 and 'Location' in response.headers):
        raise
    
    link = response.headers['Location']
    filename = link.split('/')[-1]
    response = requests.head(link, allow_redirects=False, headers=headers2)
    if not (300 <= response.status_code < 400 and 'Location' in response.headers):
        raise
        
    link = response.headers['Location']
    # subprocess.run(['wget', link], check=True)
    print("wget '%s' -O %s" % (link, filename))
    