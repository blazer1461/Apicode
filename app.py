from flask import Flask, render_template, request
import steam
import youtube_v2


app = Flask(__name__)




    
@app.route("/", methods=["POST","GET"])
def main():
    if request.method=="GET":
        return render_template("basic.html")
    elif request.method=="POST":

        try:
            name = request.form["steamID"]
            (games , w ,gname) = steam.steam_return(name)
            blah = []
            for a in xrange(len(games)):
                blah.append(a)
            return render_template("search.html", list_of_games=sorted(w.iteritems(), key=(lambda s : s[1]), reverse=True), user_name= name, games= w, names=gname)
        except:
            return render_template("basic.html", Error= "You have typed in an error")


@app.route("/videos/<gameName>", methods = ["POST"])
def videos():
    while gameNamefind("%20") != -1:
        x = gameName.find("%20")
        gameName = gameName[:x] + " " + string[x+3:]
    aDict= youtube_v2.search(gameName)
    titles= aDict.keys()
    return render_template("videos.html")


if __name__ == "__main__":
    app.debug=True
    app.run()
