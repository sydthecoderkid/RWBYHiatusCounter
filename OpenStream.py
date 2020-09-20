import random
import requests
import json
from datetime import datetime

parameters = {
    "lat": 40.71,
    "lon": -74.0,
}
def connectToAPI():
     response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
     pass_times = response.json()['response']
     printinfo(pass_times)

def printinfo(obj):
  #  text = json.dumps(obj, sort_keys=True, indent=4)

    risetimes = []
    for rt in obj:
     time = datetime.fromtimestamp(rt['risetime'])
     risetimes.append(time)
     print(time)


connectToAPI()