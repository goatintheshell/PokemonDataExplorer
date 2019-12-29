from django.urls import path
from . import views

urlpatterns = [
    path("", views.predictive_index, name="predictive_index"),
    path("predictivemodel/", views.create_pmodel, name="create_pmodel"),

]