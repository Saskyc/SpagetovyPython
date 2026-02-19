from flask import Flask
from flask import render_template

from Object import Object

app = Flask(__name__)

@app.route("/")
def domov():
    return render_template("index.html",
                        nigger = "Omg",
                        page_text = "TEST OMG OMG",)

app.run()

print("test")