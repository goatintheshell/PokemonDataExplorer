from django.urls import path
from . import views

urlpatterns = [
    path("", views.scatterplot_index, name="scatterplot_index"),
    path("scatterplot/", views.create_scatterplot, name="create_scatterplot"),

]