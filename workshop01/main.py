# main.py 
import flask
import random

app = flask.Flask(__name__)

def generate_random_text():
    return random.choice(
        [
            "Logic will get you from A to B. Imagination will take you everywhere.",
            "There are 10 kinds of people. Those who know binary and those who don't.",
            "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
            "It's not that I'm so smart, it's just that I stay with problems longer.",
            "It is pitch dark. You are likely to be eaten by a grue."
        ]
    )

@app.route("/")
def render_template():
    title = generate_random_text()
    repo_link = "https://github.com/rileychin/NUSISS-containers-pre-course-assessment"
    img_src = "cat.jpg"
    return flask.render_template("base.html", title=title, repo_link=repo_link, img_src=img_src)

if __name__ == "__main__":
    app.run(debug=True)
