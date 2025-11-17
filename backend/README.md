# Django Project – Bagpack & Crochet Management

## 📌 Project Overview
This project is a **Django-based web application** designed for managing user accounts and product catalogs related to **backpacks** and **crochet items**. It provides both a web interface and a versioned API for integration and automation.

---

## ✅ Key Features
- **Account Module** – User registration, login, and logout.
- **Bagpack Module** – Manage backpacks (create, edit, view).
- **Crochet Module** – Manage crochet products.
- **Welcome Module** – Landing page with base layout.
- **API**:
  - Versioned endpoints (e.g., `/api/versions/v1/...`).
  - Swagger documentation support.
  - Custom management command `show_urls` to list all available endpoints.

---

## 🗂 Project Structure
```
├── api
│   ├── management/commands/        # Custom Django commands
│   ├── utils/                      # API utilities (Swagger, versioning)
│   ├── versions/v1/                # Versioned API endpoints
│   └── urls.py                     # API URL configuration
├── apps
│   ├── account/                    # User account module
│   ├── bagpack/                    # Backpack management module
│   ├── crochet/                    # Crochet management module
│   ├── welcome/                    # Landing page module
├── backend/settings/               # Django settings (base, dev, prod)
├── media/                          # Uploaded files
├── static/                         # Global static assets
├── scripts/                        # Helper scripts
├── manage.py                       # Django management script
└── requirements.txt                # Python dependencies
```

---

## 🔧 Requirements
- Python 3.10+
- Django 5.x
- Dependencies listed in `requirements.txt`

---

## 🚀 Installation & Setup
1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure environment variables**:
   - Create `.env.dev` or `.env.prod` based on provided examples.
4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```
5. **Run development server**:
   ```bash
   python manage.py runserver
   ```

---

## 🧪 Running Tests
To run tests:
```bash
python manage.py test
```

---

## 📚 API Documentation
- Swagger UI available at: `/api/docs/` (or configured URL).
- Command to list all endpoints:
   ```bash
   python manage.py show_urls
   ```

---

## 🔗 API Endpoints (v1)
| Endpoint                              | Method | Description                  |
|--------------------------------------|--------|-----------------------------|
| `/api/versions/v1/account/register/` | POST   | Register a new user         |
| `/api/versions/v1/account/login/`    | POST   | User login                  |
| `/api/versions/v1/bagpack/`          | GET    | List all backpacks          |
| `/api/versions/v1/bagpack/<id>/`     | GET    | Retrieve backpack details   |
| `/api/versions/v1/crochet/`          | GET    | List all crochet products   |
| `/api/versions/v1/crochet/<id>/`     | GET    | Retrieve crochet details    |

---

## 🏗 Architecture Diagram
![Architecture Diagram](architecture_diagram.png)

---

## 📦 Deployment
- Use `gunicorn` or `uwsgi` for production.
- Configure `ALLOWED_HOSTS` and set `DEBUG=False`.
- Optionally use Docker for containerized deployment.

---

## 👤 Author
Łukasz Szabat – M.Sc. Eng.

## 📜 License
MIT License (or specify your license)
