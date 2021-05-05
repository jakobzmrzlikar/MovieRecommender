from django.contrib import admin

from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('accounts/sign_up/', views.sign_up, name="sign-up")
]
