# ---------------------------------------
# -- Falsk => Intro and first web page --
# ---------------------------------------
# - Flask is micro framework built with python 
# --------------------------------------------
# - HTML
# - CSS
# - JavaScript
# --------------------------------------------

from flask import Flask

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
    return "This is flask framework"

@skills_app.route("/about")
def about():
    return "About page from flask"

if __name__ == "__main__":

    skills_app.run(debug=True, port=9000)

