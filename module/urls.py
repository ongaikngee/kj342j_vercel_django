from django.urls import path
from module.views import index

urlpatterns = [
    path('', index),
]