from flask import Flask, request, jsonify

app = Flask(__name__)


todos = []


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    task = {"id": len(todos) + 1, "task": data["task"], "completed": False}
    todos.append(task)
    return jsonify({"message": "Task added successfully!", "task": task}), 201


@app.route('/todos/<int:task_id>', methods=['PUT'])
def update_todo(task_id):
    for task in todos:
        if task["id"] == task_id:
            task["completed"] = True
            return jsonify({"message": "Task updated!", "task": task})
    return jsonify({"error": "Task not found"}), 404


@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_todo(task_id):
    global todos
    todos = [task for task in todos if task["id"] != task_id]
    return jsonify({"message": "Task deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
