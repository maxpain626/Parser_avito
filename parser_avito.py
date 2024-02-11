import urllib.request 
import urllib.parse 
import re


req = urllib.request.Request('https://www.avito.ru/moskovskaya_oblast_krasnogorsk/mototsikly_i_mototehnika/honda_cb400sf_1994_4098010592')
req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
req.add_header('Accept-Encoding', 'gzip, deflate, br')
req.add_header('Accept-Language', 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0')
req.add_header('Host', 'www.avito.ru')
req.add_header('Cookie', 'luri=moskovskaya_oblast_krasnogorsk; srv_id=onjxl4DUfdnMBCYx.rvK_XmtzjOC7Cmw4AOzBDHnvpO8CJ0c9gSdU9VvGVAATK5npUEYO1IuZkedXOCUccQXp.To1HILuYAtu2Et7aBjv2VNCPPs4i0PlRdw9MLtRqPcw=.web; u=32cmbk2b.1dkvcmz.8vvtxshrivw0; luri=all; buyer_location_id=621540; sx=H4sIAAAAAAAC%2F5zOy03EQAwA0F58zsHjz9iTbmZiG8SBgIRY0Cq9I0rYbeDp3QEpLbNkkHeNyINWj%2FCOtmYaBex3%2BIYdZjO8yQd71fl1%2FNx%2B3096%2BXwLjfM8XhE2SNiboamOhnptcITOcNfJRMGzUePukqvSMwbl47KJoV8bRGOkhcmrO2tkdZKMPmx4hRs%2Bd%2BZ%2FmRsKRj%2B0dIWolazkyhE1hKc%2FLguh2XX9BQAA%2F%2F8sbojZaQEAAA%3D%3D; _gcl_au=1.1.176071773.1707455679; advcake_track_id=6ee4544d-443a-0deb-8ec5-d15063468a34; advcake_session_id=f4a91172-ba87-9f9b-d898-af01122b03f8; _ga_M29JC28873=GS1.1.1707486618.3.1.1707488314.60.0.0; _ga=GA1.1.872562752.1707455680; tmr_lvid=7fdf9659447548e07289fcea42f83936; tmr_lvidTS=1707455679894; f=5.df155a60305e515a4b5abdd419952845a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e9a68643d4d8df96e94f9572e6986d0c624f9572e6986d0c624f9572e6986d0c62ba029cd346349f36c1e8912fd5a48d02c1e8912fd5a48d0246b8ae4e81acb9fa1a2a574992f83a9246b8ae4e81acb9fad99271d186dc1cd0e992ad2cc54b8aa8baed66fa7192f00c615ab5228c34303140e3fb81381f3591956cdff3d4067aa559b49948619279110df103df0c26013a1d6703cbe432bc2af722fe85c94f7d0c2da10fb74cac1eabdc5322845a0cba1af722fe85c94f7d0c2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab2da10fb74cac1eab3c02ea8f64acc0bd853206102760b3e6de87ad3b397f946b4c41e97fe93686ad87594f5122e1ce8ce58006f7e783421402c730c0109b9fbb72ee3aa7362eea74163c6c97e91658f99154f4aaf0a7b4f449ad91e156a03cb0b26f2f9cca2996b82ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3aefcfb0a8b1110195ea7979e8c52648973de19da9ed218fe23de19da9ed218fe2dd005b3ec641eead9c90cd6fe2c1b035ee7b7f8c455a62a8; ft="mvEqBXSfSDYU9FTxI5maXjxtgn8pYBRFDagm1Gsqi3du+rt7kUEzwOIpbHVO0cM7COSMIMYtLWpz1es6yreRX1IVLctaGyCcpJ/z+i+J1ZxephbV9VdL3aNIDckN1Yf7+VcKy3nlKgafsSQxVk+eZrEi93rpkkN38rlnjVEza7RthEpBq/OBT9cQZR6FYbgc"; _ym_uid=1707455681548059821; _ym_d=1707455681; gMltIuegZN2COuSe=EOFGWsm50bhh17prLqaIgdir1V0kgrvN; adrdel=1; adrcid=Ae0ccm8Nf2sk926gfzXCB5w; uxs_uid=23689180-c70a-11ee-b30f-e9b97831f0d2; _ym_isad=2; tmr_detect=0%7C1707488322312; v=1707488323; SEARCH_HISTORY_IDS=0; abp=0; dfp_group=46')

response = urllib.request.urlopen('https://www.avito.ru/moskovskaya_oblast_krasnogorsk/mototsikly_i_mototehnika/honda_cb400sf_1994_4098010592')

print(response.read())



test_data = '<meta itemprop="availability" content="https://schema.org/LimitedAvailability"><meta itemprop="priceCurrency" content="RUB"><span class="style-price-value-main-TIg6u"><span content="130000" itemprop="price" class="styles-module-size_xxxl-A2qfi" data-marker="item-view/item-price">130&nbsp;000<span itemprop="priceCurrency" content="RUB" class="styles-module-size_xxxl-A2qfi">&nbsp;₽&nbsp;</span></span><span class="style-price-value-additional-pFInr"></span></span>'




'''
values = {'q': 'python urllib tutorials'}

data = urllib.request.urlencode(values)
url = 'https://www.google.com/search?q='+data
#data = data.encode('utf-8')

req = urllib.request.Request(url, data)
resp = urlreq.urlopen(req)
resp_data = resp.read()
print(resp_data)

req = urlreq.urlopen('https://www.avito.ru/moskovskaya_oblast_krasnogorsk/mototsikly_i_mototehnika/honda_cb400sf_1994_4098010592')
print(req.read())

f = open('temp.txt', 'r')
content = f.read()
print(content)
'''