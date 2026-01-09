# Django Project – PLCraft Management

## 📌 Project Overview
This project is a **Django-based web application** designed for managing user accounts and product catalogs related to **backpacks** and **crochets**. It provides both a web interface and a versioned API for integration and automation.

---

## ✅ Key Features
- **Account Module** – User registration, login, and logout.
- **Bagpack Module** – Manage backpacks (create, edit, view).
- **Crochet Module** – Manage crochet products.
- **Welcome Module** – Landing page with base layout.
- **API**:
   - Versioned endpoints (e.g., `/api/...`).
   - Swagger documentation support. `/api/swagger/`
   - Redoc UI available at: `/api/redoc/`

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
2. **Create virtual evironments**:
   - python -m vevn venv
3. **Configure environment variables**:
   - Create `.env.dev` or `.env.prod` based on provided examples.
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Run development server**:
   ```bash
   python manage.py runserver
   ```

---

## 👤 Author
Lukasz Szabat

## 📜 License
MIT License
