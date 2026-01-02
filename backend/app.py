import os
from flask import Flask, render_template, request
from database import create_table, save_error, fetch_history

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# create database table once
create_table()

def explain_error(error):
    if "KeyError" in error:
        return "A dictionary key was accessed that does not exist."
    elif "TypeError" in error:
        return "An operation was attempted on incompatible data types."
    elif "IndexError" in error:
        return "A list or sequence index is out of range."
    else:
        return "Unknown runtime issue. Review logic and input data."

@app.route("/", methods=["GET", "POST"])
def home():
    explanation = None

    if request.method == "POST":
        error = request.form.get("error", "").strip()
        if error:
            explanation = explain_error(error)
            save_error(error, explanation)

    history = fetch_history()

    return render_template(
        "home.html",
        explanation=explanation,
        history=history
    )

if __name__ == "__main__":
    app.run(debug=True)
