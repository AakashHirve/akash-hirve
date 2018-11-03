import requests
import json
from bs4 import BeautifulSoup as bs
print("Hello World")
page = ""
try:
    url = "http://api.icndb.com/jokes/random"
    page = requests.get(url)
    
    response = page.text
    pyformat = json.loads(response)
    print(pyformat["value"]["joke"])
except:
    print("Error")
