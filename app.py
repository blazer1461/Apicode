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

        (games , w ,gname) = steam.steam_return(name)

        blah = []
        for a in xrange(len(games)):
            blah.append(a)

        return render_template("search.html", list_of_games=sorted(games.iteritems(), key=lambda s : s[1]), user_name= name, games= w, names=gname)


@app.route("/videos/<gameName>", methods = ["POST"])
def videos():

    '''
    aDict= youtube_v2.search(gameName)
    titles= aDict.keys()
'''
    return render_template("videos.html")
    
if __name__ == "__main__":
    app.debug=True
    app.run()
