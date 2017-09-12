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


def capchaCkeck():
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
    print(cookies)
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    # req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
    img = opener.open(req).read()
    with open('image.png', 'wb') as f:
        f.write(img)


    data['answer'] = input('Location:\n')
    data = parse.urlencode(data)
    req = urllib.request.Request(CAPTCHA_CHECK_URL)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36')
    req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
    html = opener.open(req, data=bytes(data.encode('UTF-8'))).read().decode('UTF-8')
    print(html)


def test_login():
    data = {
        'answer': '115,55,110,11',
        'login_site': 'E',
        'rand': 'sjrand'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Referer': r'https://kyfw.12306.cn/otn/login/init'
    }

    # cj = cookiejar.LWPCookieJar()
    # cookies = urllib.request.HTTPCookieProcessor(cj)
    s = requests.session()
    p = s.get('https://kyfw.12306.cn/otn/login/init#', verify=False)
    print('cookies-01:{}' % s.cookies)
    img = s.get('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.8962342237695811', verify=False).content
    print('cookies-02:{}' % s.cookies)
    with open('image.png', 'wb') as f:
        f.write(img)

    data['answer'] = input('Location:\n')
    data = parse.urlencode(data)

    print('cookies:{}' % s.cookies)
    html = s.post(CAPTCHA_CHECK_URL, data=bytes(data.encode('UTF-8')), cookies=s.cookies, headers=headers, verify=False).content.decode('UTF-8')
    print(html)
# test_login()
capchaCkeck()

