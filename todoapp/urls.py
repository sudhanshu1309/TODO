# from django.contrib import admin
from django.urls import path, include
from todoapp import views


urlpatterns = [
    path('<int:todoID>/deleteTodo',views.deleteTodo,name='deleteTodo'),
    path("export/", views.export, name="export"),
    path('', views.index, name='index'),
    path('toggleStatus/',views.toggleStatus),

]
