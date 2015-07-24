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
        temp= apicode.steamid_conversion(user)
        return render_template("games.html", username= user, games= temp)

if __name__ == "__main__":

    app.debug= True
    app.run(host= '0.0.0.0', port= 12345)
