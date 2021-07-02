from urllib.request import urlopen
import json
stringData=urlopen('http://api.exchangeratesapi.io/v1/latest?access_key=143b32ba3d580c4d5d6f77f89761f1a4').read()
jsonData=json.loads(stringData)
print(type(jsonData))
print(jsonData)
