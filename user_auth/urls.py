"""rpn47_forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include

from .views import start_page, user_login, user_logout

urlpatterns = [
    path('', start_page, name='start_page'),
    path('login', user_login, name='user_login'),
    path('logout', user_logout, name='user_logout'),
    path('accounts/login/', start_page, name='start_page'),

]

