# 🚀 FastAPI CRUD Application

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
</p>

A highly performant, robust, and scalable CRUD (Create, Read, Update, Delete) RESTful API built with Python and FastAPI. This project serves as an excellent foundation for building data-driven backend applications with automatic interactive documentation.

## ✨ Features
- **Lightning Fast:** Built on top of Starlette and Pydantic for maximum performance.
- **Automatic Docs:** Fully interactive API documentation provided by Swagger UI and ReDoc out-of-the-box.
- **Data Validation:** Strict type checking and request validation utilizing Pydantic models.
- **Database Integration:** Seamless ORM integration for standard database operations.

## 🛠️ Local Development Setup

To run this API locally on your machine, follow these steps:

1. **Clone the repository**
   ```bash
   git clone https://github.com/varunvamin/fast_API_CRUD.git
   cd fast_API_CRUD
   ```
2. **Create a virtual environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Start the Uvicorn server**
   ```bash
   uvicorn main:app --reload
   ```
5. **Access the API Docs**
   Navigate to `http://127.0.0.1:8000/docs` in your browser to interact with the API endpoints!

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).