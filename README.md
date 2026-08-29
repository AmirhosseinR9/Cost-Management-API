# 📊 Cost Management API

A simple API for managing costs with CRUD operations (Create, Read, Update, Delete).

---

## 📖 Project Description

This is a practice project for learning **FastAPI** and **Pydantic**.  
Data is stored temporarily in memory (In-Memory) and will be lost after server restart.

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **FastAPI** (for building the API)
- **Pydantic V2** (for data validation)
- **Uvicorn** (for running the server)

---

## 🚀 Installation & Running

```bash
# 1. Clone the repository
git clone https://github.com/your-username/cost-management-api.git
cd cost-management-api

# 2. Install dependencies
pip install fastapi uvicorn

# 3. Run the application
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