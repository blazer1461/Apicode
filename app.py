from flask import Flask, render_template, request
import steam
import youtube_v2


app = Flask(__name__)

    
@app.route("/", methods=["POST","GET"])
def main():
    if request.method=="GET":
        return render_template("basic.html", Error = "Enter steam username ")
    elif request.method=="POST":
        try:
            name = request.form["steamID"]
            w = steam.steam_return(name)
            return render_template("search.html", list_of_games=sorted(w.items(), key=(lambda s : s[1]), reverse=True))
        except:
            return render_template("basic.html", Error= "NOT FOUND")

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
    app.run(host = "0.0.0.0")
