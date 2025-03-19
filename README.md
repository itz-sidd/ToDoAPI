```markdown
# 📝 To-Do List API

A simple To-Do List REST API built using Flask that allows users to manage their daily tasks efficiently. This API supports adding, updating, deleting, and filtering tasks.

## 🚀 Features
- 📌 Add tasks with priority, due dates, and categories
- ✅ Mark tasks as completed
- 🔍 Filter tasks based on status
- 📊 View task statistics (completed vs pending)
- 🎉 Get motivational messages when completing tasks

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **API Testing:** Postman / cURL

## 📂 Project Structure
```
📁 todo-api
│── app.py          # Main Flask application
│── requirements.txt # Dependencies
│── README.md        # Project documentation
```

## 🏗️ Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/todo-api.git
   cd todo-api
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```
   The API will be available at **http://127.0.0.1:5000**.

## 📌 API Endpoints
| Method | Endpoint       | Description |
|--------|--------------|-------------|
| GET    | `/todos`      | Get all tasks |
| POST   | `/todos`      | Add a new task |
| PUT    | `/todos/<id>` | Mark a task as completed |
| DELETE | `/todos/<id>` | Delete a task |
| GET    | `/stats`      | View task completion stats |

### 🔹 Example: Add a Task (POST)
```json
{
  "task": "Finish Python Project",
  "priority": "High",
  "due_date": "2025-03-20",
  "category": "Work"
}
```

### 🔹 Example: Mark Task as Completed (PUT)
```sh
curl -X PUT http://127.0.0.1:5000/todos/1
```




