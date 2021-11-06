"""url_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import django.contrib.auth.views as auth_views
from url_shortener_app.views import *

urlpatterns = [
    path('',homepage),
    path('<url_key>', perform_redirect),
    path('app/admin', admin.site.urls),
    path('app/login', auth_views.LoginView.as_view(template_name='login.html')),
    path('app/register', create_user),
    path('app/url-tool', get_url_tool_page),
    path('app/logout', logout_user),
]
