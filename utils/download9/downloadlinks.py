import os
import requests
import subprocess
from parse import search


headers1 = {"Cookie": r'''cookie for download.oracle.com'''}
headers2 = {"Cookie": r'''cookie for edelivery.oracle.com'''}
data = r'''//download.oracle.com/otn/java/jdk/10.0.2+13/19aef61b38124481863b1413dce1855f/jdk-10.0.2_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10.0.2+13/19aef61b38124481863b1413dce1855f/jre-10.0.2_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10.0.2+13/19aef61b38124481863b1413dce1855f/serverjre-10.0.2_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/jdk-10.0.1_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/jre-10.0.1_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/serverjre-10.0.1_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10+46/76eac37278c24557a3c4199677f19b62/jdk-10_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10+46/76eac37278c24557a3c4199677f19b62/jre-10_linux-x64_bin.tar.gz
//download.oracle.com/otn/java/jdk/10+46/76eac37278c24557a3c4199677f19b62/serverjre-10_linux-x64_bin.tar.gz
'''


for link in data.split('\n'):
    link = 'https:' + link.strip()
    if not search('jdk-{}_linux-x64_bin.tar.gz', link):
        continue
        
    r = search('https://download.oracle.com/otn/java/jdk/{}/{}/jdk-{}_linux-x64_bin.tar.gz', link)
    if r is None:
        continue
        
    if r[2] == '10.0.1':
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
    