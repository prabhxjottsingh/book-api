"""
URL configuration for book_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home_page

# Defining URL patterns for the project using a list called 'urlpatterns'.
urlpatterns = [
    # URL pattern for the Django admin site, accessible at '/admin/'
    path('admin/', admin.site.urls),

    # Default URL pattern for the project's root URL ('/'). Maps to the 'home_page' view.
    path('', home_page),

    # URL pattern for the 'api' app, including its URLs. This allows access to the API endpoints.
    path('api/', include('api.urls')),
]
