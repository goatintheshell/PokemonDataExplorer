from django.urls import path
from . import views

urlpatterns = [
    path("", views.boxplot_index, name="box_index"),
    path("boxplot/", views.create_boxplot, name="create_boxplot"),

]