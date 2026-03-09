# 📒 FastAPI Notes API

A simple **Notes REST API** built using **FastAPI, SQLAlchemy, and SQLite**.

This project demonstrates how to build a backend service with **CRUD operations** using FastAPI and a relational database.

The API allows users to:

- Create notes
- Retrieve all notes
- Retrieve a specific note
- Update a note
- Delete a note

---

# 🚀 Features

- FastAPI based backend
- SQLite database
- SQLAlchemy ORM
- Pydantic data validation
- Full CRUD operations
- Beginner-friendly project structure

---

# 🛠 Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

---

# 📂 Project Structure

```
fastapi-notes-api/
│
├── main.py
├── notes.db
└── README.md
```

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-notes-api.git
cd fastapi-notes-api
```

---

### 2. Create a virtual environment (optional)

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

---

# ▶️ Run the API

Start the server using:

```bash
uvicorn main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

# 📑 API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

# 📌 API Endpoints

## Root

```
GET /
```

Response:

```
{
  "message": "Notes API is running"
}
```

---

## Create Note

```
POST /Notes
```

Request body:

```json
{
  "title": "My Note",
  "content": "This is the content of the note"
}
```

---

## Get All Notes

```
GET /notes
```

Returns all stored notes.

---

## Get Specific Note

```
GET /notes/{id}
```

Example:

```
GET /notes/1
```

---

## Update Note

```
PUT /notes/{id}
```

Query Parameters:

```
u_title
u_content
```

Example:

```
PUT /notes/1?u_title=Updated Title&u_content=Updated Content
```

---

## Delete Note

```
DELETE /notes/{id}
```

Example:

```
DELETE /notes/1
```

---

# 🧠 What I Practiced in This Project

- Building APIs with **FastAPI**
- Using **SQLAlchemy ORM**
- Implementing **CRUD operations**
- Data validation with **Pydantic**
- Backend API development with Python

---

# 📜 License

This project is created for **learning and practice purposes**.