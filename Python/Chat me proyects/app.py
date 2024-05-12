from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = ['Completar proyecto', 'Estudiar Python', 'Hacer ejercicio']

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    new_task = request.form["task"]
    tasks.append(new_task)
    return redirect(url_for("index"))

@app.route("/delete_task", methods=["POST"])
def delete_task():
    task_to_delete = request.form["task"]
    tasks.remove(task_to_delete)
    return redirect(url_for("index"))

@app.route("/complete_task", methods=["POST"])
def complete_task():
    completed_task = request.form["task"]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
