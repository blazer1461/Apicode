import urllib2
import json
w= {}
API_KEY = "2152FCF9797139E2F079D0345F438F72"

def steamid_conversion(username):
    steam_id_url= "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + API_KEY + "&vanityurl="+username
    url_open= urllib2.urlopen(steam_id_url)
    result= url_open.read();
    steam_id_params=json.loads(result)
    t = steam_id_params["response"]["steamid"]
    steam_url= "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + API_KEY + "&steamid="+t+" &format=json&include_played_free_games=1"
    url_open= urllib2.urlopen(steam_url)
    result= url_open.read();
    steam_params=json.loads(result)
    dict= steam_params["response"]
    return dict

def getAppList():
    url= "http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    url_open=urllib2.urlopen(url)
    result= url_open.read();
    steam_names= json.loads(result)
    return steam_names["applist"]["apps"]["app"]

def binary_search_appid(alist, id):
    start = 0
    end = len(alist) - 1
    while (end >= start):
        mid = (end - start) / 2 + start
        if alist[mid]['appid'] == id:
            # found it
            return alist[mid]['name']
        if alist[mid]['appid'] > id:
            end = mid -1
        else:
            start = mid + 1
    # if we are here (outside the while loop), then we didn't find it
    return None

def steam_return(user):
        dict = steamid_conversion(user)
        game_dict= dict["games"]
        w= {}
        x = 0.0
        gname={}
        name_id = getAppList()
        for item in game_dict:
            appid= item["appid"]
            playtime= item["playtime_forever"]
            x = float(playtime) / 60
            x = round(x, 1)
            w[appid]= x
            gname[appid] = binary_search_appid(name_id, appid)
        games= gname.values()
        return games, w, gname

    

