from flask import Flask, render_template, request
from utils import braille


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    arrays = braille()

    keys_arrays = arrays.keys()

    phrase = ""
    if request.method == "POST":
        phrase = request.form["phrase"]

        return render_template(
            "index.html", arrays=arrays, phrase=phrase, keys_arrays=keys_arrays
        )

    return render_template("index.html", arrays=arrays, keys_arrays=keys_arrays)


if __name__ == "__main__":
    app.run(debug=True)
