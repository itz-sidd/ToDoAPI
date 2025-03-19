from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample To-Do List (in-memory storage)
todos = []

motivational_quotes = [
    "Great job! Keep going! 🚀",
    "You're unstoppable! 🔥",
    "Another step closer to success! 💪",
    "Well done! Time to tackle the next one! ✅"
]

# Route to get all tasks
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Route to add a new task
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = {
        "id": len(todos) + 1,
        "task": data.get("task", "Untitled Task"),
        "completed": False,
        "priority": data.get("priority", "Medium"),  # Default priority
        "due_date": data.get("due_date", "No deadline"),  # Default due date
        "category": data.get("category", "General")  # Default category
    }
    todos.append(task)
    return jsonify({"message": "Task added successfully!", "task": task}), 201

# Route to mark a task as completed
@app.route('/todos/<int:task_id>', methods=['PUT'])
def update_todo(task_id):
    for task in todos:
        if task["id"] == task_id:
            task["completed"] = True
            message = random.choice(motivational_quotes)
            return jsonify({"message": message, "task": task})
    return jsonify({"error": "Task not found"}), 404

# Route to delete a task
@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_todo(task_id):
    global todos
    todos = [task for task in todos if task["id"] != task_id]
    return jsonify({"message": "Task deleted successfully!"})

# Route to get task completion stats
@app.route('/stats', methods=['GET'])
def task_stats():
    completed = sum(1 for task in todos if task["completed"])
    pending = sum(1 for task in todos if not task["completed"])
    return jsonify({"Completed Tasks": completed, "Pending Tasks": pending})

if __name__ == '__main__':
    app.run(debug=True)


