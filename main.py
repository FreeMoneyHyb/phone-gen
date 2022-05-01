import requests
import random
import time




print("[§] Loading Free HTTP Proxies If U Want Them")
time.sleep(.5)
proxya = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=500&country=all&ssl=all&anonymity=all")
print(proxya.text)
print("[§] Loading Free Socks4 Proxies If U Want Them")
time.sleep(.5)
proxy3 = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=500&country=all&ssl=all&anonymity=all")
print(proxy3.text)
print("[§] Loading Free Socks5 Proxies If U Want Them")
time.sleep(.5)
proxy4 = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=500&country=all&ssl=all&anonymity=all")
print(proxy4.text)
print("[§] Loading Free HTTPS Proxies If U Want Them")
time.sleep(.5)
proxy5 = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=https&timeout=250&country=all&ssl=all&anonymity=all")
print(proxy5.text)




test_headers = {}
geokeys = (['e35aa5dabc1646b6be9da8fbef3ba4d9','ff6f9bf65f6d4eb2a671b36ceedadf9f','962421ffa7f243e6b6b79458aefa38c1','92d2e33be85c41b28b09034cef57babf','726b510f4dee4dffadbcaf989d0ec43e'])
ggs = random.choice(geokeys)
geo = requests.get(f"https://ipgeolocation.abstractapi.com/v1/?api_key={ggs}")
ba1 = geo.json()['city']
ba2 = geo.json()['region']
ba3 = geo.json()['ip_address']
ba4 = geo.json()['security']
timee = requests.get(f"https://www.timeapi.io/api/Time/current/ip?ipAddress={ba3}")

bb1 = timee.json()['time']
bb2 = timee.json()['dayOfWeek']
bb3 = timee.json()['timeZone']

print(f'''FMH v1.5.5

 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████      ▄████ ▓█████  ███▄    █ 
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀     ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███      ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░      ░ ░   ░    ░      ░   ░ ░ 
          ░  ░  ░    ░ ░           ░    ░  ░         ░    ░  ░         ░ 
The only free phone gen and checker on the internet......................                                                                         

---------
IP DATA : {ba3} {ba1}, {ba2}
Time DATA : {bb1} {bb3}, {bb2} 
Current Api's : Abstract, Proxyscrape, TimeApi 
Current Imports : Time, Random, Requests
New Shit : More Api Keys + Gui Rework
---------

''')
time.sleep(1)
print('''





[!] Starting''')
time.sleep(.3)
with open(f"numbers.txt", "w", encoding='utf-8') as file:
  areacode = (['205','251','256','334','938','907','480','520','602','623','928','479','501','870','209','213','279','310','323','408','415','424','442','510','530','559','562','619','626','628','650','657','661','669','707','714','747','760','805','818','820','831','858','909','916','925','949','951','303','719','720','970','203','475','860','959','302','239','305','321','352','386','407','561','727','754','772','786','813','850','863','904','941','954','229','404','470','478','678','706','762','770','912','808','208','986','217','224','309','312','331','618','630','708','773','779','815','847','872','219','260','317','463','574','765','812','930','319','515','563','614','712','316','515','563','641','712','316','630','708','773','779','815','847','872','219','260','317','463','574','765','812','930','319','515','563','641','712','316','620','785','913','270','364','502','606','859','225','318','337','504','985','207','240','301','410','443','667','339','351','413','508','617','774','781','857','978b','231','248','269','313','517','586','616','734','810','906','947','989','218','320','507','612','651','763','952','228','601','662','769','314','417','573','636','660','816','406','308','402','531','702','725','775','603','201','551','609','640','732','848','856','862','908','973','505','575','212','315','332','347','516','518','585','607','631','646','680','716','718','838','845','914','917','929','934','252','336','704','743','828','910','919','980','984','701','216','220','234','330','380','419','440','513','567','614','740','937','405','539','580','918','458','503','541','971','215','223','267','272','412','445','484','570','610','717','724','814','878','401','803','843','854','864','605','423','615','629','731','865','901','931','210','214','254','281','325','346','361','409','430','432','469','512','682','713','726','737','806','817','830','832','903','915','936','940','956','972','979','385','435','801','802','276','434','540','571','703','757','804','206','253','360','425','509','564','202','304','681','262','414','534','608','715','920','307'])
  acckey = (['0a13700965984e83b0321b67d8ec6146','305159c53ea24881aed0f91bc5958042','b51314ddf11c4d27a6b0d6e772b2d5ac','42b1c0fefb994e1e9ea0d92731e3ae5d','3d16b5e9c9be4c30aa0f85f02002ff86','4ded31c790ac4ac1b298b06a49059a0e','2466d199bcff40a985764ee12db62e6d','5d90fd86a9bb4b3784fde014e74df8c0','0ae9ad9e100b4a9d9093c2d123d577a6','3b5fc5785be241ba8a16eafa8ef9a763','77a7b7357a4c43e4bcee55f5f303aed2','dbdd26ee907f41c88f82ab9ff8028dee','23f1af18821145d4847301b577ebcaf5','22fa2afe5a3d4bc6bfd3c3b4ed352e14','eac91fe723af4a1a88060717eacbf8fe','d4bbd9255e9f4ece824b39200c0b8f5c','a3fd0fc246694d34b46124c950f8972f','861d16f895494fa48e206ad5b29cf587','00225e6a67354b8a866b13eb99b6746c','843ff30eb54e4b00af04c28cbfac6256','dd499c1a46474b3791e1982106df7a39','6be0e1858430406dba1fa1e54a8937ff','4a64ea5e511b4b7189c66b18852682d8','066d51f2b0ae42e68560a4ec4671b7c0','9ebb97bc790442928a0d7b3206a59b3a','74c93996652a4ecbb5f6bfd439edf1aa','4de73d80daa948a28e1e1c2c5348f596','f089eb478a02490791579fda3cc810d0','c971730398da4a4693ef60b5f2b494cf','7fa8e0066ee34b6cb0e61da8225a509b','2d08c80f853140e6a62c5dca23b83477','5f4668acdf064082904b4241c1381d90','77358879717749f8a66fa422336266b6','e9c20b43e2ee4d11820c0879bfc3f6d4','fa7cb20dbdde4ad691799b9120c7b010','5e97f093ebdb4eba944f666e3ab29563','6f8ca91a6ec34e68abd3c99a525a537e','d2e083d6634240a886e8c544d01d203c','b8e743215c4340929612e3b5686d540e','215d97245d324205a8a9593a998d567e','0be09511b4f0463b985d13b2d0a40e76','4db95bcc0581433185be1dfbd57a57ba','0692ddecd64343e2a6bf7f5d6f104144','6dc14a5bf54a4b7b9f9fac2b831a3316','0cace00c3137490583e28e5b539b397c','c0d1a37357ee44778649c1cfdc5eb049','eba6a0604e514f74b482ab09aac0ef2d','db1150f59de84d24b24c6a6978fafdf2','802320cab5db41f481ffdadd20019602','9d27cdc68db04843a3e4ef67843ac677','952dc2c2b12f4778b17ba311db230bc4','95eb023f1f244a7c97236e1623063630','479b22a26ef14bea964f1b3294c9631f','0495237cc4744c199dde62f339a685c7','a17e5d4220af4550a5aa9d9b5b10aa8f','876d1bfc3333414fa2b458a14bdf95e5','c154ce28ca144299a4e0fc19c4149218','a02a9bc0b6694283b9c1e9a42a0345bd','38407669aea64984bfa76ecd1ef29e59','93db901737b54b7daf2c4695236641f3','82ea92080c1743c4834dd6697f4ef2bf','6a446d3b492a4730b160681540ec9042','fdf7b0ed9912452486cefabdcae07b9c','09ced01ff57a4b2fa43a86914c9ad7a2','73883e0dd16548cb97b09496c16a541a','e92776e191304ba885e52ef5b4e1571f','87342e4cb52c4090a5326431380b8294','78d8ef76d490472fb96d677a02ba1fce','73c337fc19eb4cd5b0dcab0f422b5a54','be8a482a6bdb4d56b948fc4650d5458b','73bbe4dc650544e2a3b94554846a459c','069210de7e7646beb8f24a95819223df','a18ba8c879e6481d85b6c7c3b19c3160','c58d427986e148778a7cd38685006348','2a9fbfd584924b379e08d72f3fe361d1','d9f82e43730343a8ada53d0295dfd18d','63abe5cf1a784917a2322c836af34584','b830858d307c4569b515864da562f8f0','a442b3847bc945b892d677e1c2a24da2','cff9e7f2375542b781846b48127136e3','2948b4d61b394420b91dd6aeea7f18a6','175a50143e9948c19429b7da4c2ce078','112c058452c3422a9b40e25d52ace0c5','52b1a4ca1b994760a7e5472edebe980e','20b4101605404f6aaca06d8d793df3b9','fc2984e5848348be96b724533d63562e'])
  hh = int("99999999999")
  for i in range(hh):
    time.sleep(.9)
    office = random.randint(200,999)
    sub = random.randint(1000,9999)
    jmao = random.choice(acckey)
    mainc = random.choice(areacode)
    numberz = f"1{mainc}{office}{sub}"
    wood = f"{mainc}{office}{sub}"
    h = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key={jmao}&phone={numberz}")   

 
    if h.status_code==200:
      br1 = h.json()['valid']
      br2 = h.json()['location'] 
      br3 = h.json()['type']
      br4 = h.json()['carrier']
           
            
      if br3 == "mobile":
        print(f'''<{i}>[§] GOOD NUMBER! - {wood}''')        
        file.write(f"{wood}\n")
        print(f'<{i}>[§] Added {wood} To numbers.txt')            
        print(f'''<{i}>[§] Info On {wood} {br4}/{br2},USA/{br3}''')
        
             
      if br3 == "unknown":
        print(f"<{i}>[!] Number {wood} Invalid")
      if br3 == "voip":        
        print(f"<{i}>[!] Number {wood} Is Voip (bot number)")
      if br3 == "landline":
        print(f"<{i}>[!] Number {wood} Is A Landline (building phone)")
      else:
        nothing = random.randint(0,1)
        
      
      
  
    
    else: 
      print(f"<{i}>[!] Key {jmao} Rate Limited ")
      
  
for line in file.readlines():
  idk = line.strip("\n")  
  
      
