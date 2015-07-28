from flask import Flask, render_template, request
import steam
import youtube

app = Flask(__name__)

@app.route("/")
def main():

    return render_template("basic.html")

@app.route("/search", methods = ["POST"])
def search():
    name = request.form["steamID"]
    games = youtube.steam_return(name)
    blah = []
    for a in xrange(len(games)):
        blah.append(a)
    return render_template("search.html")

@app.route("/videos/<gameName>", methods = ["POST"])
def videos():

    return render_template("videos.html")
    
if __name__ == "__main__":
    app.run()
