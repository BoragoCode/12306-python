import requests
import ssl
import json
import urllib
from urllib import request
import urllib3
from http import cookiejar
from urllib import parse
import io
from PIL import Image


CAPTCHA_CHECK_URL = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
# 信任12306的证书信息
ssl._create_default_https_context = ssl._create_unverified_context


def capchaCkeck_urllib():
    data = {
        'answer': '115,55,110,11',
        'login_site': 'E',
        'rand': 'sjrand'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Referer': r'https://kyfw.12306.cn/otn/login/init'
    }

    cj = cookiejar.LWPCookieJar()
    cookies = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(cookies)
    req = urllib.request.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8962342237695811')
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    # req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
    img = opener.open(req).read()
    print(cookies)
    with open('image.png', 'wb') as f:
        f.write(img)


    data['answer'] = input('Location:\n')
    data = parse.urlencode(data)
    req = urllib.request.Request(CAPTCHA_CHECK_URL)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
    html = opener.open(req, data=bytes(data.encode('UTF-8'))).read().decode('UTF-8')

    print(html)


def test_login_requests():
    data = {
        'answer': '115,55,110,1',
        'login_site': 'E',
        'rand': 'sjrand'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Referer': r'https://kyfw.12306.cn/otn/login/init'
    }

    s = requests.session()
    p = requests.get('https://kyfw.12306.cn/otn/login/init#', verify=False)
    rsp = s.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8962342237695811', verify=False)
    img = rsp.content
    with open('image.png', 'wb') as f:
        f.write(img)

    data['answer'] = input('Location:\n')
    html_rsp = s.post(CAPTCHA_CHECK_URL, data=data, headers=headers, verify=False)
    html = html_rsp.content.decode('UTF-8')
    print(html)



test_login_requests()
# capchaCkeck()

