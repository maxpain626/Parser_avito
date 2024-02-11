from urllib.request import Request, urlopen
import urrlib.parse


req = Request('https://www.avito.ru/moskovskaya_oblast_krasnogorsk/mototsikly_i_mototehnika/honda_cb400sf_1994_4098010592')
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0')
#req.add_header('', '')
#req.add_header('', '')
#req.add_header('', '')
#req.add_header('', '')

