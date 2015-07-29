import urllib2
import json

API_KEY = "AIzaSyBtPQJ1yx9sAqRVSCMQdcPB6BqFUVhERIg"

def search(query):
    fixed = ""
    if query.find(" ") != -1:
        for char in query:
            if char == " ":
                fixed += "+"
            else:
                fixed += char

    temp = urllib2.open("https://www.googleapis.com/youtube/v3/search?videoEmbeddable=true&part=id%2Csnippet&q=" + fixed + "&type=video&maxResults=10&key=" + API_KEY)
    temp2 = temp.read()
    temp3 = json.loads(data)
    data = temp3["items"]
    link = "https://www.youtube.com/watch?v="
    vids = {}
    for x in data:
        xlink = link + x["id"]["videoId"]
        name = x["snippet"]["title"]
        vids[name] = xlink
    return vids
