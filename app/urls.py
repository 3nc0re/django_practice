from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.universal, name="universal"),
    path('add_medicine/', views.add_medicine, name="add_medicine"),
    path('add_organization/', views.add_organization, name="add_organization"),
    path('display_medicine_for_organization/', views.display_medicine_for_organization, name="display_medicine_for_organization"),
    path('display_organizations_for_medicine/', views.display_organizations_for_medicine, name="display_organizations_for_medicine"),

]