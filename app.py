__author__ = 'blazer1461'
import apicode
from flask import Flask, render_template, request

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

app= Flask (__name__)

@app.route("/", methods=["POST", "GET"])

def steam_return():
    if request.method == "GET":
        return render_template("base.html", username="Steam Search")
    elif request.method == "POST":
        user= request.form["username"]
        dict= apicode.steamid_conversion(user)
        s= dict["game_count"]
        game_dict= dict["games"]
        w= {}
        for i in range(s):
            appid= game_dict[i]["appid"]
            playtime= game_dict[i]["playtime_forever"]
            w[appid]= playtime
        #binary search tree that allows the appids to be converted to game names.

        name_id= apicode.converting_ids_to_names()
        binary_search_appid(name_id, game_dict["appid"])



        return render_template("games.html", username= user, games= w)

if __name__ == "__main__":

    app.debug= True
    app.run(host= '0.0.0.0', port= 12345)
