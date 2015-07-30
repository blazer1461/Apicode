import urllib2
import json
w= {}
API_KEY = "2152FCF9797139E2F079D0345F438F72"

def steamid_conversion(username):
    steam_id_url= "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + API_KEY + "&vanityurl="+username
    url_open= urllib2.urlopen(steam_id_url)
    result= url_open.read();
    steam_id_params=json.loads(result)
    steamID = steam_id_params["response"]["steamid"]
    steam_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + API_KEY + "&steamid=" + steamID + "&format=json&include_played_free_games=1&include_appinfo=1"
    url_open= urllib2.urlopen(steam_url)
    result= url_open.read();
    steam_params=json.loads(result)
    dict= steam_params["response"]
    return dict

def steam_return(user):
        dict = steamid_conversion(user)
        game_dict= dict["games"]
        print game_dict
        w= {}
        x = 0.0
        gname={}
        for item in game_dict:
            name= item["name"]
            playtime= item["playtime_forever"]
            x = float(playtime) / 60
            x = round(x, 1)
            w[name]= x
        games= w.keys()
        return games, w

    

