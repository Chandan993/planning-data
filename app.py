from flask import Flask, render_template, request
from agents.planner_agent import generate_study_plan

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        subject = request.form["subject"]
        hours = request.form["hours"]

        plan = generate_study_plan(subject, hours)

        return render_template("plan.html", subject=subject, plan=plan)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
