from django.contrib import admin
from .views import *
from django.urls import path, include


urlpatterns = [
    path('', index, name='home'),
    path('rubric/<int:rubric_id>/', rubric, name='rubric'),
    path('rubrics/', rubrics, name='rubrics'),
    path('dishes/<int:dish_id>', show_dish, name='dish'),
    path('dishes/', dishes, name='dishes'),
]