__author__ = 'blazer1461'
import urllib2
import json


def steamid_conversion(username):
    steam_id_url=


def steam_api(id):
    steam_url= "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2152FCF9797139E2F079D0345F438F72&steamid="id" &format=json"
    url_open= urllib2.urlopen(steam_url)
    steam_params=json.loads(url_open)
    return steam_params[""][""]

