from flask import Flask,  render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return """
    <p>Paulo: GNU (GNU, Not ,Unix)</p>
    <p>Moises: IYKYK (If,You,Know,You,Know)</p>
    <p>Miguel: TTYL (Talk, To, You, Later)</p>
    """

@app.route("/kalyn")
def kalyn():
    favorite_acronym = "LOL"
    return render_template("templates.html", acronym=favorite_acronym)

if __name__ == "__main__":
    app.run(debug=True)