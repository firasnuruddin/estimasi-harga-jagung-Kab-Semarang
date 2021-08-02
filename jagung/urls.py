
from os import name
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('form/', views.form_page, name="form-predict"),
    path('form/submit', views.predict, name="submit-predict")
]
