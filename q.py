import requests
import sys

to = str(sys.argv[0])
file = str(sys.argv[1])
rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=all&timeout='+str(to))
with open(str(file),'wb') as fp:
	fp.write(rsp.content)
	print("GenerateProxy : Success")
