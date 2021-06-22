# ------------------------------------
# -- Falsk => Jinja template engine --
# ------------------------------------


from flask import Flask, render_template

skills_app = Flask(__name__)

my_skills = [("HTML", 80), ("CSS", 75), ("Python", 90)]

@skills_app.route("/")
def homepage():
    return render_template("homepage.html", 
                            title="Homepage", 
                            test="This is a",
                            costum_css="home")

@skills_app.route("/add")
def add():
    return render_template("add.html", 
                            pagetitle="add page",
                            costum_css="add")

@skills_app.route("/about")
def about():
    return render_template("about.html", 
                            title="About", 
                            test="This is b")

@skills_app.route("/skills")
def skills():
  return render_template("skills.html",
                          title="My skills",
                          page_head="My skills",
                          description="The is my skill page",
                          skills=my_skills)


if __name__ == "__main__":

    skills_app.run(debug=True, port=9000)

