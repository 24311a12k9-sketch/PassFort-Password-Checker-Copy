
from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password(password):

    rules = {
        "At least 8 characters": len(password) >= 8,
        "One uppercase letter": bool(re.search(r"[A-Z]", password)),
        "One lowercase letter": bool(re.search(r"[a-z]", password)),
        "One digit": bool(re.search(r"[0-9]", password)),
        "One special character": bool(re.search(r"[^A-Za-z0-9\s]", password)),
        "No whitespace": not bool(re.search(r"\s", password))
    }

    score = sum(rules.values())

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return rules, strength


@app.route("/", methods=["GET", "POST"])
def home():

    rules = {}
    strength = ""
    password = ""

    if request.method == "POST":

        password = request.form.get("password", "")

        rules, strength = check_password(password)

    return render_template(
        "index.html",
        rules=rules,
        strength=strength,
        password=password
    )


if __name__ == "__main__":
    app.run(debug=True)
