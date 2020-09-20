import random
import requests
import json
import pytumblr
from datetime import datetime


def connectToAPI():
   client = pytumblr.TumblrRestClient('04jDlKiLcnVV6hYsLtPiBz198r8Y4Uc8HPGQxhIe9GXfW1gC8i')
   callAPI(client)
   
 
   

def callAPI(obj):
   print("HERE")
   print(obj.blog_info('sydthecoderkid.tumblr.com'))


    
