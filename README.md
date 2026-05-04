# Advance_Database_Management_System
Advance_Database_Management_System


🚀 Django REST Framework (DRF) API Setup Guide
📌 Step-by-Step Installation (Windows CMD)

🔹 1. Create Virtual Environment

Open Command Prompt
Run:
python -m venv env

 2. Activate Virtual Environment
    cd env
cd Scripts
activate

3. Install Django & DRF
   pip install django djangorestframework

 4. Verify Installation
    pip list

5. Create Django Project
   django-admin startproject api

   6. Navigate to Project Folder
      cd api

  7. Create Django App
     python manage.py startapp app

8. Open Project in VS Code
Drag and drop the complete api folder into VS Code
Or run:
 
drf-yasg - Yet another Swagger generator

Usage
0. Installation
The preferred installation method is directly from pypi:

pip install -U drf-yasg


1. Quickstart
In settings.py:

INSTALLED_APPS = [
   ...
   'django.contrib.staticfiles',  # required for serving swagger ui's css/js files
   'drf_yasg',
   ...
]

main urls.py


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

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
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
<img width="2550" height="3300" alt="Advance Database Managment System Course Outline" src="https://github.com/user-attachments/assets/66dbd4f4-3e9e-4288-8b4d-00792526a8cf" />
