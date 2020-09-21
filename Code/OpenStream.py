import random
import requests
import json
import pytumblr
from datetime import datetime
import datetime
from datetime import date

def connectToAPI():
   client = pytumblr.TumblrRestClient('04jDlKiLcnVV6hYsLtPiBz198r8Y4Uc8HPGQxhIe9GXfW1gC8i')
   callAPI(client)
  
   

def callAPI(obj):
    bloginfo = obj.blog_info('rwbyhiatuscountdown.tumblr.com')
    title = "Blog was last updated:"
    print(title, datetime.datetime.fromtimestamp(bloginfo['blog']['updated']))
    print("Today is:", date.today())
    print(bloginfo['blog']['title'])
 
     
          





connectToAPI()
    
