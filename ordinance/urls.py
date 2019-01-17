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

from django.urls import path

from .views import ordinance_form, get_inn, ordinance_save

urlpatterns = [
    # path('/<str:msg>/<slug:raspr_num_1>/<slug:raspr_num_2>', bylaw_form, name='bylaw_form_pa'),
    # path('/<str:msg>/', bylaw_form, name='bylaw_form_pa'),
    # path('/get_inn', get_inn, name='get_inn'),
    path('/ordinance_save', ordinance_save, name='ordinance_save'),
    path('', ordinance_form, name='ordinance_form'),
]

