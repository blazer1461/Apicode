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

@app.route("/video/<gameName>")
def videos(gameName):
    if gameName.find("%20") != -1:
        while gameName.find("%20") != -1:
            x = gameName.find("%20")
            gameName = gameName[:x] + " " + string[x+3:]
    result = youtube_v2.search(gameName)
    blah = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    linx = result[0]
    titles = result[1]
    return render_template("videos.html", blah = blah, linx = linx, titles = titles)


if __name__ == "__main__":
    app.debug=True
    app.run(host = "0.0.0.0")
