__author__ = 'blazer1461'
import urllib2
import json

def steam_api(user):
    steam_url= "" #put in url here
    url_open= urllib2.urlopen(steam_url)
    steam_params=json.loads(url_open)
    return steam_params[""][""]