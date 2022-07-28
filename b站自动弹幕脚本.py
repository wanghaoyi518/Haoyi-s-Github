import requests
import time
import random
# 自动发送的弹幕内容
list_text = ['666', '加油',
            '拼了',
            '好好学习',
            '天天向上',
            '一定能行']
 

def send():
    a = 0
    while True:
        # 发送的间隔时间
        time.sleep(10)
        send_mesg = random.choice(list_text)
        url = 'https://api.live.bilibili.com/msg/send'
        data = {
            'bubble': '0',
            'msg': send_mesg,
            'color':'16777215',
            'mode': '1',
            'fontsize': '25',
            'rnd': '1658976501',
            'roomid': '24813410',
            'csrf': 'e20ab3ebe3190537e14888b351429ce5',
            'csrf_token': 'e20ab3ebe3190537e14888b351429ce5',
        }
 
        headers = {
            'cookie': 'buvid3=6F78C7C3-88F6-8BDF-6C17-F766BE6940FD90078infoc; i-wanna-go-back=-1; _uuid=2C89B164-4EB7-C26A-1101E-CCFEC8C4F2D1090314infoc; buvid4=9AFA3A45-F6F0-1F74-4256-6589783EC0F590875-022061816-4osVj//bpYZ7QMzhuinRnw%3D%3D; sid=alz09tos; fingerprint=70aabaf2e2b60ec7d843d37b2391e2cd; buvid_fp_plain=undefined; DedeUserID=313051405; DedeUserID__ckMd5=8f2c57e91d0d830e; SESSDATA=40c0bf93%2C1671092750%2C53c10*61; bili_jct=e20ab3ebe3190537e14888b351429ce5; buvid_fp=5ef8042f1712805869d94af0c50fc9fe; b_ut=5; nostalgia_conf=-1; CURRENT_BLACKGAP=0; blackside_state=0; CURRENT_QUALITY=80; rpdid=|(kmRYRYJ)ll0J\'uYlllRY|mm; LIVE_BUVID=AUTO2116555464830622; hit-dyn-v2=1; is-2022-channel=1; bp_video_offset_313051405=687547603240353800; bsource=share_source_weixinchat; _dfcaptcha=62477bbaba4067dc98a4a2002bf02a10; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1658720727,1658807563,1658901108,1658975489; b_lsid=110374F19_18242AEF5A0; innersign=1; b_timer=%7B%22ffp%22%3A%7B%22333.788.fp.risk_6F78C7C3%22%3A%2218242AFCD9E%22%2C%22333.1007.fp.risk_6F78C7C3%22%3A%2218242A41CAE%22%2C%22444.7.fp.risk_6F78C7C3%22%3A%2218242A44C20%22%2C%22444.55.fp.risk_6F78C7C3%22%3A%2218242A45883%22%2C%22333.337.fp.risk_6F78C7C3%22%3A%2218242A4A4D1%22%2C%22444.8.fp.risk_6F78C7C3%22%3A%2218242A4B93B%22%7D%7D; CURRENT_FNVAL=4048; PVID=10; Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02=1658976505',
            'origin': 'https://live.bilibili.com',
            'referer': 'https://live.bilibili.com/25278623?hotRank=0&session_id=17fc341fef0f4ad5e6434b99c0295905_2A304024-5370-4802-9110-233E6BB68399&launch_id=1000154&visit_id=a1xj41rdews0',
            ##'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            ##'sec-ch-ua-mobile': '?0',
            ##'sec-ch-ua-platform': '"Windows"',
            ##'sec-fetch-dest': 'empty',
            ##'sec-fetch-mode': 'cors',
            ##'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
        result=requests.post(url=url,data=data,headers=headers)
        print(result.text)
if __name__=='__main__':
    send()
 