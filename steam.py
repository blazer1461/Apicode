from urllib.request import urlopen
import json
w= {}
API_KEY = "6FC10D5A75E6EC09D63D83EED8AD418E"

def steamid_conversion(username):
    steam_id_url= "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=" + API_KEY + "&vanityurl="+username
    result= urlopen(steam_id_url).read()
    steam_id_params=json.loads(result)
    steamID = steam_id_params["response"]["steamid"]
    steam_url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + API_KEY + "&steamid=" + steamID + "&format=json&include_played_free_games=1&include_appinfo=1"
    print("got here too")
    url_open= urlopen(steam_url).read()
    steam_params=json.loads(url_open)
    dict= steam_params["response"]
    return dict

def steam_return(user):
        dict = steamid_conversion(user)
        game_dict= dict["games"]
        w= {}
        x = 0.0
        gname={}
        for item in game_dict:
            name= item["name"]
            playtime= item["playtime_forever"]
            x = float(playtime) / 60
            x = round(x, 1)
            w[name]= x
        return w

    

