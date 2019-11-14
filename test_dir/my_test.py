from urllib import request
import json

web_url= request.urlopen('http://www.nbrb.by/api/exrates/currencies')
data = web_url.read()
data = data.decode()
data_structure = json.loads(data)

print(data_structure[0]['Cur_ID'])
print(type(data_structure))
print(len(data_structure))
print(data_structure[0])
print(type(data_structure[0]))