from urllib.request import urlopen
from pprint import pprint
import json


with urlopen("https://www.example.com") as response:
    pass

pprint(response.headers["Server"])
#pprint(response.getheader("Server"))
#pprint(response.headers.items())


'''
with urlopen("https://www.example.com") as response:
    pprint(dir(response))
'''

'''
url = "https://jsonplaceholder.typicode.com/todos/1"
with urlopen(url) as response:
    body = response.read()
    
json_item = json.loads(body)
print(json_item)
'''

'''
with urlopen("https://www.example.com") as response:
    body = response.read()
    print(body[:15])
'''