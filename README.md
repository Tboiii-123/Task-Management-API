# 📝 Task Management API

This is a simple and powerful Task Management REST API built with Django and Django REST Framework.  
It allows users to sign up, log in, and manage their tasks easily.

---

## 🚀 Features

- User Signup & Login (Token Authentication)
- Create, Update, Delete Tasks
- List and Filter Tasks by Status (Complete/Incomplete)
- Email Notification When Task is Marked as Complete
- Interactive API Docs with Swagger (drf_yasg)

---

## 🔧 Tech Stack

- Python 3.9+
- Django 4.x
- Django REST Framework
- drf-yasg (Swagger Docs)
- SQLite (default DB)

---

## 📦 Installation

1. Clone the repo  
   git clone https://github.com/your-username/task-api.git  
   cd task-api

2. Create a virtual environment  
   python -m venv venv  
   venv\Scripts\activate  (on Windows)

3. Install dependencies  
   pip install -r requirements.txt

4. Apply migrations  
   python manage.py migrate

5. Run the server  
   python manage.py runserver

---

## 🔑 Authentication

All task-related endpoints require a token.

1. Sign up at:  
   POST /signup/

2. Log in to get your token:  
   POST /login/

3. Use your token in the Authorization header:  
   Authorization: Token your_token_here

---

## 📬 API Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| POST   | /signup/            | Register a new user      |
| POST   | /login/             | Login and get token      |
| GET    | /api/tasks/         | List your tasks          |
| POST   | /api/tasks/         | Create a new task        |
| PUT    | /api/tasks/<id>/    | Update a task            |
| PATCH  | /api/tasks/<id>/    | Partially update a task  |
| DELETE | /api/tasks/<id>/    | Delete a task            |

---

## 📘 Swagger Documentation

You can explore and test the API using Swagger:

http://127.0.0.1:8000/swagger/

Use the "Authorize" button to paste your token like this:  
Token your_token_here

---




## 📄 License

This project is open-source and available under the MIT License.

---

## 🙋‍♂️ Author

Lawal Hussein Taiwo  
Python Django Developer  
GitHub: https://github.com/Tboiii-123 
LinkedIn: https://linkedin.com/in/lawal-hussein  
Portfolio: https://tboiii-porfolio.vercel.app/
