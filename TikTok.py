from email.message import Message 
from requests import * 
from user_agent import * 
from random import * 
from time import * 
from names import * 
import requests
import json
import os

Token = input("[×] Enter Youe Token :- ")
IDdd = input("[×] Enter Your Id :- ")
os.system('clear')
class alaa:
    def Tik(email): 
        coder = "https://www.tiktok.com/passport/web/user/check_email_registered?shark_extra=%7B%22aid%22%3A1459%2C%22app_name%22%3A%22Tik_Tok_Login%22%2C%22app_language%22%3A%22en%22%2C%22device_platform%22%3A%22web_mobile%22%2C%22region%22%3A%22SA%22%2C%22os%22%3A%22ios%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Fprofile%22%2C%22root_referer%22%3A%22https%3A%2F%2Fwww.google.com%22%2C%22cookie_enabled%22%3Atrue%2C%22screen_width%22%3A390%2C%22screen_height%22%3A844%2C%22browser_language%22%3A%22en-us%22%2C%22browser_platform%22%3A%22iPhone%22%2C%22browser_name%22%3A%22Mozilla%22%2C%22browser_version%22%3A%225.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2014_4%20like%20Mac%20OS%20X%29%20AppleWebKit%2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Version%2F14.0.3%20Mobile%2F15E148%20Safari%2F604.1%22%2C%22browser_online%22%3Atrue%2C%22timezone_name%22%3A%22Asia%2FRiyadh%22%2C%22is_page_visible%22%3Atrue%2C%22focus_state%22%3Atrue%2C%22is_fullscreen%22%3Afalse%2C%22history_len%22%3A17%2C%22battery_info%22%3A%7B%7D%7D&msToken=vPgBDLGXZNEf56bl_V4J6muu5nAYCQi5dA6zj49IuWrw2DwDUZELsX2wz2_2ZYtzkbUF9UyblyjQTsIDI5cclvJQ6sZA-lHqzKS1gLIJD9M6LDBgII0nxKqCfwwVstZxhpppXA==&X-Bogus=DFSzsIVLC8A-dJf6SXgssmuyRsO1&_signature=_02B4Z6wo00001dTdX3QAAIDBDn9.7WbolA3U3FvAABfU8c" 
        data = f"email={email}&aid=1459&language=en&account_sdk_source=web&region=SA" 
        Check_Tik = post(coder,headers={"User-Agent": str(generate_user_agent())},data=data).text 
         
        if '{"is_registered":1}' in Check_Tik: 
            return { 
                "Message":"Available","Email":email 
                } 
 
        elif '{"is_registered":0}' in Check_Tik: 
            return { 
                "Message":"Not Available","Email":email
                } 
 
        else: 
            return { 
                "Message":"Blocked","Email":email 
                } 
    def yahoo(Email): 
        rd= { 
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '17973',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8','Cookie': 'APID=UP139a7583-ebf0-11eb-b505-06ebe7a65878; B=1gu92j5gg4sv7&b=3&s=64; A1=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; A3=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk; GUC=AQEBAQFg_FZhBEIc3QQ6; cmp=t=1627550703&j=0; APIDTS=1627550737; A1S=d=AQABBCoF-2ACEDfMWHRNdZQ9oaAHUO4YHqMFEgEBAQFW_GAEYQAAAAAA_eMAAAcI53MCYZkieRg&S=AQAAAuJmx1yIDVMiY71k2AGooYk&j=WORLD; AS=v=1&s=9z9sgq95&d=A6103d241|eavlddr.2Sqtm1snR4vumZPgWEv2CX8ETv8qsCVpXUOAi6BcDaqYAawFRdXZOH3x1ZhIOOPANiSybHZ1j1IBJfKp_yUQeVT2a7U2iFeceXk3DV8Yf6fdA4Mb3M_1A3WY2rpfLpkN2geA1AHRb_QuK0p_gvRBC25hCJqX6_BqNWBCQZ40y2vcTOUrMHZQRGCPbygJ4jCC1pmj16D_TNVaFo68GkkgrxHiFpLQEP9zBsfEM9g8FM8Qd3Gs8oJHQRyvyel09x3uEdniEFCXR93nRCcOMMKCI7xvW239gVcz1Gs_5hmZv6aql00Zge0HJaK6YKPDg9Q7rFfMe7pJry4gCuNMiq_bH9TeBHQEGjqLCJR_d8hcSFHxUnNah4D8.hwV7o1hyYUKQl2Pw6aVKPizRyscmuz0Rwa1LUKGV0O2ls2MSsR4g4TzVlLObvUuKBdrdIJJD3Em1NsNsXKj3uyr.XgZV3E09rJQbldIcePNMPkT7jJjydoGuIBVbqutW0MgHN5IShbRcy6cVifEmil4551or5xaGO5kNpIDCbjUmhD8.MnIfBGRlSIITVGGoQhj3l5TBA742dFc_zcZJmtF5XIrHTr_wMpbpc3ZzD1SgWTDMvySFcsTwH8DdIPhUw4c5QUfyh0kECQFV6OG2M9B06c1wayVg_OiVhy6B6u8Q5AHjbRhsacLtI8K7KxG3JA6oxXmOla3MUX35XvU2axN9DChrM3gpJlJYgmqxV454FF23dysnz4sixK8tvwUc.4EiOU_5OfNGmgZpA.MiCif_oYX3m92DAi38QIl~A',
    'Host': 'login.yahoo.com',
    'Origin': 'https://login.yahoo.com',
    'Referer': 'https://login.yahoo.com/account/create?.lang=ar-JO&src=homepage&specId=yidReg&done=https%3A%2F%2Fwww.yahoo.com',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': str(generate_user_agent()),
    'X-Requested-With': 'XMLHttpRequest'} 
        ata = {'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":1,"hardwareConcurrency":2,"timezoneOffset":-180,"timezone":"Asia/Baghdad","sessionStorage":1,"localStorage":1,"indexedDb":1,"openDatabase":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":3,"hash":"e43a8bc708fc490225cde0663b28278c"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc.~Google SwiftShader","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":0,"hasLiedBrowser":0,"touchSupport":{"points":0,"event":0,"start":0},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"1366","h":"768"},"availableResolution":{"w":"728","h":"1366"},"ts":{"serve":1627553991633,"render":1627553997166}}', 
    'specId': 'yidreg', 
    'crumb': 'rak/FdAmWa5', 
    'acrumb': '9z9sgq95', 
    'done': 'https://www.yahoo.com', 
    'attrSetIndex': '0', 
    'tos0': 'oath_freereg|xa|ar-JO', 
    'yid': str(Email.split('@yahoo.com')[0]), 
    'password': 'basha07', 
    'shortCountryCode': 'AF',} 
        eq = post("https://login.yahoo.com/account/module/create?validateField=yid'",headers=rd,data=ata).text 
        if ('"yid"') in eq: 
            return { 
                "Message":"Not Available_Yahoo","Email":Email} 
        else: 
            return { 
                "Message":"Available_Yahoo","Email":Email} 
    def User_Info(Usr,Token,IDd,cookies):
        User = str(Usr).split('@')[0]
        Do = str(Usr).split('@')[1]
        url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7159321838730921477&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={User}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=t_ekYkVEA-cffW1k3FGiNmUWCW4CSoNY2s_cZDEI4bghVCC3ukUwuCpKmvU7or6kdX_LjEi-Y-IIu1m0YzoG8sFwr7qyd6o5UVeaYemcBTyFYKMx20l6-aGARfLwtql1gsP-czMRJmzv1Wn_&X-Bogus=DFSzswVLxFXANj0yS0hLEAF1zKC6&_signature=_02B4Z6wo000019nDj0AAAIDDAO7.jW5QNMPZw4vAAJUe0b' 
        req=get(url,headers={'accept':'*/*',
'origin':'https://www.tiktok.com',
'referer':'https://www.tiktok.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'},cookies=cookies).json()['user_list'] 
        for i in req: 
            h = i['user_info']['unique_id'] 
            if h == f'{User}': 
                user = str(i['user_info']['unique_id']) 
                id = str(i['user_info']['uid']) 
                name = str(i['user_info']['nickname']) 
                bayo = str(i['user_info']['signature']) 
                follower = str(i['user_info']['follower_count']) 
                tex='- USER : '+str(user)+"\n"+f"- Email : {User}{Do}"+"\n"+'- ID : '+str(id)+'\n'+'- NAME : '+str(name)+'\n'+'- BAYO : '+str(bayo)+'\n'+'- FOLLOWERS : '+str(follower)+'\n'+'- LINK ACC : '+f'https://www.tiktok.com/@{user}' 
                for c in i['user_info']['avatar_thumb']['url_list']: 
                    sora=get(c) 
                with open('tiktok.jpg','wb') as sor: 
                    sor.write(sora.content) 
                post(f'https://api.telegram.org/bot{Token}/sendDocument?chat_id={IDdd}&caption={tex}', files={'document':open('tiktok.jpg', 'rb')}) 
                os.system("rm -rf tiktok.jpg") 
    def User_From_Search_yahoo(cookies):
        z = str(''.join(choice("asdfghjklmnbvcxzpoiuytrewq") for i in range(randint(3,11))))
        gg = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name(),z]))
        url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7159321838730921477&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={gg}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=t_ekYkVEA-cffW1k3FGiNmUWCW4CSoNY2s_cZDEI4bghVCC3ukUwuCpKmvU7or6kdX_LjEi-Y-IIu1m0YzoG8sFwr7qyd6o5UVeaYemcBTyFYKMx20l6-aGARfLwtql1gsP-czMRJmzv1Wn_&X-Bogus=DFSzswVLxFXANj0yS0hLEAF1zKC6&_signature=_02B4Z6wo000019nDj0AAAIDDAO7.jW5QNMPZw4vAAJUe0b' 
        req=requests.get(url,headers={'accept':'*/*',
'origin':'https://www.tiktok.com',
'referer':'https://www.tiktok.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'},cookies=cookies).json()['user_list'] 
        for i in req:
            h = i['user_info']['unique_id']
            alaa.Run1(h)
      
    def User_From_Search_Gmail(cookies):
        z = str(''.join(choice("asdfghjklmnbvcxzpoiuytrewq") for i in range(randint(3,11))))
        gg = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name(),z]))
        url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7159321838730921477&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={gg}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=t_ekYkVEA-cffW1k3FGiNmUWCW4CSoNY2s_cZDEI4bghVCC3ukUwuCpKmvU7or6kdX_LjEi-Y-IIu1m0YzoG8sFwr7qyd6o5UVeaYemcBTyFYKMx20l6-aGARfLwtql1gsP-czMRJmzv1Wn_&X-Bogus=DFSzswVLxFXANj0yS0hLEAF1zKC6&_signature=_02B4Z6wo000019nDj0AAAIDDAO7.jW5QNMPZw4vAAJUe0b' 
        req=requests.get(url,headers={'accept':'*/*',
'origin':'https://www.tiktok.com',
'referer':'https://www.tiktok.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'},cookies=cookies).json()['user_list'] 
        for i in req:
            h = i['user_info']['unique_id']
            alaa.Run3(h)
    def User_From_Search_Mail(cookies):
        z = str(''.join(choice("asdfghjklmnbvcxzpoiuytrewq") for i in range(randint(3,11))))
        gg = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name(),z]))
        url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7159321838730921477&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={gg}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=t_ekYkVEA-cffW1k3FGiNmUWCW4CSoNY2s_cZDEI4bghVCC3ukUwuCpKmvU7or6kdX_LjEi-Y-IIu1m0YzoG8sFwr7qyd6o5UVeaYemcBTyFYKMx20l6-aGARfLwtql1gsP-czMRJmzv1Wn_&X-Bogus=DFSzswVLxFXANj0yS0hLEAF1zKC6&_signature=_02B4Z6wo000019nDj0AAAIDDAO7.jW5QNMPZw4vAAJUe0b' 
        req=requests.get(url,headers={'accept':'*/*',
'origin':'https://www.tiktok.com',
'referer':'https://www.tiktok.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'},cookies=cookies).json()['user_list'] 
        for i in req:
            h = i['user_info']['unique_id']
            alaa.Run4(h)
    def User_From_Search_bk(cookies):
        z = str(''.join(choice("asdfghjklmnbvcxzpoiuytrewq") for i in range(randint(3,11))))
        gg = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name(),z]))
        url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7159321838730921477&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={gg}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=t_ekYkVEA-cffW1k3FGiNmUWCW4CSoNY2s_cZDEI4bghVCC3ukUwuCpKmvU7or6kdX_LjEi-Y-IIu1m0YzoG8sFwr7qyd6o5UVeaYemcBTyFYKMx20l6-aGARfLwtql1gsP-czMRJmzv1Wn_&X-Bogus=DFSzswVLxFXANj0yS0hLEAF1zKC6&_signature=_02B4Z6wo000019nDj0AAAIDDAO7.jW5QNMPZw4vAAJUe0b' 
        req=requests.get(url,headers={'accept':'*/*',
'origin':'https://www.tiktok.com',
'referer':'https://www.tiktok.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'},cookies=cookies).json()['user_list'] 
        for i in req:
            h = i['user_info']['unique_id']
            alaa.Run5(h)
    def User_From_Search_inbox(cookies):
        z = str(''.join(choice("asdfghjklmnbvcxzpoiuytrewq") for i in range(randint(3,11))))
        gg = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name(),z]))
        url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7159321838730921477&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={gg}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=t_ekYkVEA-cffW1k3FGiNmUWCW4CSoNY2s_cZDEI4bghVCC3ukUwuCpKmvU7or6kdX_LjEi-Y-IIu1m0YzoG8sFwr7qyd6o5UVeaYemcBTyFYKMx20l6-aGARfLwtql1gsP-czMRJmzv1Wn_&X-Bogus=DFSzswVLxFXANj0yS0hLEAF1zKC6&_signature=_02B4Z6wo000019nDj0AAAIDDAO7.jW5QNMPZw4vAAJUe0b' 
        req=requests.get(url,headers={'accept':'*/*',
'origin':'https://www.tiktok.com',
'referer':'https://www.tiktok.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'},cookies=cookies).json()['user_list'] 
        for i in req:
            h = i['user_info']['unique_id']
            alaa.Run6(h)
        	   
            
    def Gmail(emai):
    	
    	headers = {'Content-Length':'98','Content-Type':'text/plain; charset=UTF-8','Host':'android.clients.google.com','Connection':'Keep-Alive','user-agent':'GoogleLoginService/1.3(m0 JSS15J)'};data = json.dumps({'username':emai,'version':'3','firstName':'Alaabasha','lastName':'Alaabasha'})
    	check = post('https://android.clients.google.com/setup/checkavail',data=data,headers=headers)
    	if check.json()['status'] == 'SUCCESS':
		              return { 
                "Message":"Available","Email":emai 
                }
    	else:
		      return { 
                "Message":"Not Available","Email":emai
                }
    def hotmail(us):
    	emai=str(us)+'@hotmail.com'
    	
    	out = get(f"https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={us}&_=1604288577990",data = {''},headers = {"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36","Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}).text
    	if 'Neither' in out:
    		return { 
                "Message":"Available","Email":emai 
                }
    	else:
    	           return { 
                "Message":"Not Available","Email":emai
                }
    def outlook(us):
    	emai=str(us)+'@outlook.com'
    	
    	out = get(f"https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress={us}&_=1604288577990",data = {''},headers = {"Accept": "*/*","Content-Type": "application/x-www-form-urlencoded","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36","Connection": "close","Host": "odc.officeapps.live.com","Accept-Encoding": "gzip, deflate","Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0","Accept-Language": "ar,en-US;q=0.9,en;q=0.8","canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c","uaid": "d06e1498e7ed4def9078bd46883f187b","Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"}).text
    	if 'Neither' in out:
    		return { 
                "Message":"Available","Email":emai 
                }
    	else:
    	           return { 
                "Message":"Not Available","Email":emai
                }
    def all(cookies):
        z = str(''.join(choice("asdfghjklmnbvcxzpoiuytrewq") for i in range(randint(3,11))))
        gg = str(choice([get_first_name(),get_full_name().replace(' ',''),get_last_name(),z]))
        url=f'https://www.tiktok.com/api/search/user/full/?aid=1988&app_language=ar&app_name=tiktok_web&battery_info=1&browser_language=ar-AE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%206.1%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F107.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&cursor=0&device_id=7159321838730921477&device_platform=web_pc&focus_state=true&from_page=search&history_len=5&is_fullscreen=false&is_page_visible=true&keyword={gg}&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=IQ&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=768&screen_width=1366&tz_name=Asia%2FBaghdad&webcast_language=ar&msToken=t_ekYkVEA-cffW1k3FGiNmUWCW4CSoNY2s_cZDEI4bghVCC3ukUwuCpKmvU7or6kdX_LjEi-Y-IIu1m0YzoG8sFwr7qyd6o5UVeaYemcBTyFYKMx20l6-aGARfLwtql1gsP-czMRJmzv1Wn_&X-Bogus=DFSzswVLxFXANj0yS0hLEAF1zKC6&_signature=_02B4Z6wo000019nDj0AAAIDDAO7.jW5QNMPZw4vAAJUe0b' 
        req=requests.get(url,headers={'accept':'*/*',
'origin':'https://www.tiktok.com',
'referer':'https://www.tiktok.com/',
'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/92.0.0.0'},cookies=cookies).json()['user_list'] 
        for i in req:
            h = i['user_info']['unique_id']
            alaa.Run1(h)
            alaa.Run3(h)
            alaa.Run4(h)
            alaa.Run5(h)
            sleep(5)
            

    def Run1(us):
            usr=str(us)+"@yahoo.com"
            try:
            	sleep(3)
            	YH = alaa.yahoo(usr)
            	if YH['Message']=="Available_Yahoo":
            	   print('\033[1;33m'f'Available In Yahoo => {usr}') 
            	   TK = alaa.Tik(usr)
            	   if TK['Message']=='Available': 
            	       print('\033[2;32m'+f'Available In TikTok => {usr}') 
            	       try: 
                            c = alaa.Cookies()['Cookies']
                            
                            alaa.User_Info(usr,Token,IDdd,c)
            	       except requests.exceptions.ConnectionError:
                       	print("- YOUR NET IS SO BAD !")
            	   elif TK['Message']=='Not Available':
            	   	print("\033[1;97m"+f'NoT Available In TikTok => {usr}') 
            	   elif YH['Message']=="Not Available_Yahoo":
            	   	print('\033[1;31m'+f"Not Available In Yahoo => {usr}") 
            except requests.exceptions.ConnectionError:
            	print("- YOUR NET IS SO BAD !") 
    def Run3(usr):
        usr=str(usr)+"@gmail.com"
        
        try:
            sleep(3)
            YH = alaa.Gmail(usr)
            
            if YH['Message']=="Available": 
                print('\033[1;33m'f'Available In Gmail => {usr}') 
                TK = alaa.Tik(usr) 
                if TK['Message']=='Available': 
                    print('\033[2;32m'+f'Available In TikTok => {usr}') 
                    try: 
                            c = alaa.Cookies()['Cookies']
                            
                            alaa.User_Info(usr,Token,IDdd,c)
                    except requests.exceptions.ConnectionError: 
                            print("- YOUR NET IS SO BAD !") 
                elif TK['Message']=='Not Available': 
                    print("\033[1;97m"+f'NoT Available In TikTok => {usr}') 
            elif YH['Message']=="Not Available": 
                    print('\033[1;31m'+f"Not Available In Gmail => {usr}") 
             
        except requests.exceptions.ConnectionError: 
            print("- YOUR NET IS SO BAD !")
    def Run4(us):
    	usr=str(us)+"@outlook.com"
    	try:
            sleep(3)
            YH = alaa.outlook(usr)            
            if YH['Message']=="Available": 
                print('\033[1;33m'f'Available In OutLook => {usr}') 
                TK = alaa.Tik(usr) 
                if TK['Message']=='Available': 
                    print('\033[2;32m'+f'Available In TikTok => {usr}') 
                    try: 
                            c = alaa.Cookies()['Cookies']
                            
                            alaa.User_Info(usr,Token,IDdd,c)
                    except requests.exceptions.ConnectionError: 
                            print("- YOUR NET IS SO BAD !") 
                elif TK['Message']=='Not Available': 
                    print("\033[1;97m"+f'NoT Available In TikTok => {usr}') 
            elif YH['Message']=="Not Available": 
                    print('\033[1;31m'+f"Not Available In OutLook => {usr}") 
            else: 
                print(YH) 
    	except requests.exceptions.ConnectionError: 
            print("- YOUR NET IS SO BAD !")
    def Run5(us):
    	usr=str(us)+"@hotmail.com"
    	try:
            sleep(3)
            YH = alaa.hotmail(usr)            
            if YH['Message']=="Available": 
                print('\033[1;33m'f'Available In HotMail => {usr}') 
                TK = alaa.Tik(usr) 
                if TK['Message']=='Available': 
                    print('\033[2;32m'+f'Available In TikTok => {usr}') 
                    try:
                            c = alaa.Cookies()['Cookies']
                            
                            alaa.User_Info(usr,Token,IDdd,c) 
                    except requests.exceptions.ConnectionError: 
                            print("- YOUR NET IS SO BAD !") 
                elif TK['Message']=='Not Available': 
                    print("\033[1;97m"+f'NoT Available In TikTok => {usr}') 
            elif YH['Message']=="Not Available": 
                    print('\033[1;31m'+f"Not Available In HotMail => {usr}")
            
    	except requests.exceptions.ConnectionError: 
            print("- YOUR NET IS SO BAD !")
    def Run6(us):
    	usr=str(us)+"@hotmail.com"
    	try:
            sleep(3)
            YH = alaa.hotmail(usr)            
            if YH['Message']=="Available": 
                print('\033[1;33m'f'Available In HotMail => {usr}') 
                TK = alaa.Tik(usr) 
                if TK['Message']=='Available': 
                    print('\033[2;32m'+f'Available In TikTok => {usr}') 
                    try: 
                            c = alaa.Cookies()['Cookies']
                            
                            alaa.User_Info(usr,Token,IDdd,c) 
                    except requests.exceptions.ConnectionError: 
                            print("- YOUR NET IS SO BAD !") 
                elif TK['Message']=='Not Available': 
                    print("\033[1;97m"+f'NoT Available In TikTok => {usr}') 
            elif YH['Message']=="Not Available": 
                    print('\033[1;31m'+f"Not Available In HotMail => {usr}")
            
    	except requests.exceptions.ConnectionError: 
            print("- YOUR NET IS SO BAD !")
    def Cookies():
    	cookie=(get('https://www.tiktok.com',headers={'user-agent':str(generate_user_agent())}))
    	tt_csrf_token=cookie.cookies.get_dict()["tt_csrf_token"];tt_chain_token=cookie.cookies.get_dict()["tt_chain_token"];_abck=cookie.cookies.get_dict()["_abck"];bm_sz=cookie.cookies.get_dict()["bm_sz"];ttwid=cookie.cookies.get_dict()["ttwid"]
    	cookies={'cookie':'tt_csrf_token='+tt_csrf_token+'; s_v_web_id=verify_lan0kdpo_46eiYnyw_ra5d_4cyh_8Txb_c0pr1wLwfR6o; passport_csrf_token=f2b927c323b1027a37b4543df004f21c; passport_csrf_token_default=f2b927c323b1027a37b4543df004f21c; tt_chain_token='+tt_chain_token+'; _abck='+_abck+'; bm_sz='+bm_sz+'; ttwid='+ttwid+'; msToken=q5GOBCP2ysOmE3SMNg2BsyI9q-CG-g0XZeZ5-drFEHzivKFOZ2mB-jbidUqYYJgTyAUMvGeBAAoh-xjSm_X1rrWoj9XvldMQWTAzI6RTRw-LEabc98ZLk1NHzMse3nDbaOLQriM9E8v5RTYQ'}; return {'Cookies':cookies}
    	
    def Start_Tool():
        A = '\033[2;32m'
        j = '\033[2;35m'
        E = '\033[1;31m'
        bk = input(f'{j}(1) CHECK AVAILABILITY => {A}YAHOO •\n{j}(2) CHECK AVAILABILITY => {A}GMAIL •\n{j}(3) CHECK AVAILABILITY => {A}OUTLOOK •\n{j}(4) CHECK AVAILABILITY => {A}HOTMAIL •\n{j}(5) CHECK AVAILABILITY => {A}ALL DOMINS •\n------------------------------\n{E}| CHOOSE BRO =>  ') 
        os.system('clear')
        if bk == '1':
            while True:
            		try:
            			c = alaa.Cookies()['Cookies']
            			alaa.User_From_Search_yahoo(c)
            		except requests.ConnectionError:
            			print("- Your Net So Bad ! ")
            			sleep(3)
        elif bk == '2':
            while True:
            	try:
            		c = alaa.Cookies()['Cookies']
            		alaa.User_From_Search_Gmail(c)
            	except requests.ConnectionError:
            		print("- Your Net So Bad ! ")
            		sleep(3)
        elif bk == '3':
        	while True:
            		try:
            			c = alaa.Cookies()['Cookies']
            			alaa.User_From_Search_Mail(c)
            		except requests.ConnectionError:
            			print("- Your Net So Bad ! ")
            			sleep(3)
        elif bk == '4':
            while True:
            		try:
            			c = alaa.Cookies()['Cookies']
            			alaa.User_From_Search_bk(c)
            		except requests.ConnectionError:
            			print("- Your Net So Bad ! ")
            			sleep(3)
        
        elif bk == '5':
        	   while True:
            		try:
            			c = alaa.Cookies()['Cookies']
            			alaa.all(c)
            		except :
            			print("- Your Net So Bad ! ")
            			sleep(3)
        else:
            print(j+"Wrong choice !")
            sleep(3)
            os.system('clear')
            alaa.Start_Tool()
            


         		
alaa.Start_Tool()