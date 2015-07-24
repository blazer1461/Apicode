__author__ = 'blazer1461'
import urllib2
import json
w= {}


def steamid_conversion(username):
    steam_id_url= "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=2152FCF9797139E2F079D0345F438F72&vanityurl="+username
    url_open= urllib2.urlopen(steam_id_url)
    result= url_open.read();
    steam_id_params=json.loads(result)
    t = steam_id_params["response"]["steamid"]
    steam_url= "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=2152FCF9797139E2F079D0345F438F72&steamid="+t+" &format=json"
    url_open= urllib2.urlopen(steam_url)
    result= url_open.read();
    steam_params=json.loads(result)
    dict= steam_params["response"]
    return dict

def converting_ids_to_names():
    url= "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    url_open=urllib2.urlopen(url)
    result= url_open.read();
    steam_names= json.loads(result)
    return steam_names["applist"]["apps"]["app"]