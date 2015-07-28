from flask import Flask, render_template, request
import steam
import youtube

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def main():
    if request.method=="GET":
        return render_template("basic.html")
    elif request.method=="POST":
        name = request.form["steamID"]
        games = steam.steam_return(name)
        blah = []
        for a in xrange(len(games)):
            blah.append(a)
        return render_template("search.html")


@app.route("/videos/<gameName>", methods = ["POST"])
def videos():

    return render_template("videos.html")
    
if __name__ == "__main__":
    app.debug= True
    app.run(host= '0.0.0.0', port= 12345)
