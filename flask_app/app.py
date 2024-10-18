

from flask import Flask, render_template, request, redirect, url_for
from task_manager import TaskManager  # Import the TaskManager class

app = Flask(__name__)

# Create an instance of TaskManager
task_manager = TaskManager()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the task details from the form
        title = request.form["title"]
        description = request.form["description"]
        
        # Add the task using the TaskManager
        task_manager.add_task(title, description)
        return redirect(url_for("index"))  # Redirect to the index page after adding task
    
    # Get the list of tasks to display
    tasks = task_manager.get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/delete", methods=["POST"])
def delete_task():
    title = request.form["title"]
    task_manager.remove_task(title)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
