# 🚀 Advance Database Management System  
## Django REST Framework (DRF) API Setup Guide

This repository provides a step-by-step guide to setting up a Django REST Framework (DRF) API with Swagger documentation using drf-yasg.

---

## 📌 Prerequisites

- Python 3.x  
- pip  
- VS Code (or any IDE)

---

## ⚙️ Step-by-Step Installation (Windows CMD)

### 🔹 1. Create Virtual Environment
```bash
python -m venv env
```

### 🔹 2. Activate Virtual Environment
```bash
cd env
cd Scripts
activate
```

### 🔹 3. Install Django & DRF
```bash
pip install django djangorestframework
```

### 🔹 4. Verify Installation
```bash
pip list
```

### 🔹 5. Create Django Project
```bash
django-admin startproject api
```

### 🔹 6. Navigate to Project Folder
```bash
cd api
```

### 🔹 7. Create Django App
```bash
python manage.py startapp app
```

### 🔹 8. Open Project in VS Code
```bash
code .
```

---

## 📚 API Documentation with Swagger (drf-yasg)

### 🔹 Installation
```bash
pip install -U drf-yasg
```

---

### 🔹 Configure `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
]
```

---

### 🔹 Configure `urls.py`

```python
from django.contrib import admin
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0),
            name='schema-json'),

    path('swagger/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),

    path('redoc/',
         schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
```

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

---

## 🌐 API Documentation URLs

- Swagger UI: http://127.0.0.1:8000/swagger/  
- ReDoc UI: http://127.0.0.1:8000/redoc/  

---

## 📂 Project Structure

```
api/
│── api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
│── app/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
│── manage.py
```

---

## 🖼️ Course Outline

![Course Outline](https://github.com/user-attachments/assets/66dbd4f4-3e9e-4288-8b4d-00792526a8cf)

---

## 💡 Notes

- Always activate the virtual environment before working  
- Save dependencies using:
```bash
pip freeze > requirements.txt
```
- Keep your API modular using apps  

---

## 📌 Author

Adnan Majeed
