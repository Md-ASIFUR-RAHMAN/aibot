"""chatbot URL Configuration

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
from django.urls import path,include
from api import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home),
    path('register', v.reg),
    path('login_user',v.Login),
    path('faq/<str:pk>', v.faq),
    path('chatbot/<str:pk>', v.chatbot),
    path('dashboard/<str:pk>', v.dashboard),
    path('update/<str:pk>', v.update),
    path('delete/<str:pk>', v.delete),
    path('logout', v.Logout),

    path('secret/', include('chat.urls')),

]
