__author__ = 'blazer1461'
import apicode
from flask import Flask, render_template, request


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
        name_id= apicode.converting_ids_to_names()
        for i in range(s):
            appid= game_dict[i]["appid"]
            playtime= game_dict[i]["playtime_forever"]
            w[appid]= playtime




        return render_template("games.html", username= user, games= w)

if __name__ == "__main__":

    app.debug= True
    app.run(host= '0.0.0.0', port= 12345)
