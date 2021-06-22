# ------------------------------------
# -- Falsk => Jinja template engine --
# ------------------------------------


from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
    return render_template("homepage.html", title="Homepage", test="This is a")

@skills_app.route("/about")
def about():
    return render_template("about.html", title="About", test="This is b")

if __name__ == "__main__":

    skills_app.run(debug=True, port=9000)
