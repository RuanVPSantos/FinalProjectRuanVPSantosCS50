from flask import Flask, request, render_template

import csv

# our first objective is create a landding page for the apresentation.

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
#the enter of the site could be an landing page. 

if __name__ == '__main__':
    app.run()