from django.views.generic import TemplateView
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('hello/', views.hello, name = 'hello'),

]