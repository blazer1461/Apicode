__author__ = 'blazer1461'
import apicode
from flask import Flask, render_template, request

app= Flask (__name__)

@app.route("/", methods=["POST", "GET"])

def steam_return():
    if request.method == "GET":
        return render_template("base.html")
    elif request.method == "POST":

