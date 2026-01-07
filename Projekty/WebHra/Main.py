from flask import Flask
from markupsafe import Markup
import GameClasses

print("GameClasses loaded from:", GameClasses.__file__)
print("EditableEntity dir:", dir(GameClasses.EditableEntity))

editable = GameClasses.EditableEntity(0.01, 0.01, 50, 40, "Player").Show()



app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Test webu<h/1> <a href='druha''>odkaz</a>"

@app.route('/druha')
def druha():
    
    print("AAAAAAAAAAAAAA", editable)
    return editable

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)