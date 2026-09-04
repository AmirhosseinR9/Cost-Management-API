# 📊 Cost Management API

A simple API for managing costs with CRUD operations (Create, Read, Update, Delete).

---

## 📖 Project Description

This is a practice project for learning FastAPI, Pydantic, SQLAlchemy (ORM), and Alembic (migrations).
Data is now stored persistently in an SQLite database, replacing the previous in-memory storage approach.

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **FastAPI** (for building the API)
- **Pydantic V2** (for data validation)
- **Sqlalchemy** (ORM for database interaction)
- **Alembic** (for database migrations)
- **Uvicorn** (for running the server)

---

## 🚀 Installation & Running


### 1. Clone the repository
```bash
git clone https://github.com/your-username/cost-management-api.git
cd cost-management-api
```

### 2. Install dependencies
```bash
uv sync
```

### 3. Run the application
```bash
uvicorn main:app --reload
After running, the API will be available at:
➡️ http://127.0.0.1:8000

Swagger UI documentation:
➡️ http://127.0.0.1:8000/docs


📋 Available Endpoints
Method	Path	Description
POST	/cost	Create a new cost
GET	/costs	Get all costs
GET	/cost/{id}	Get a cost by ID
PUT	/cost/{id}	Update a cost
DELETE	/cost/{id}	Delete a cost
```