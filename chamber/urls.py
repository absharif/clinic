from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('search_profile/', views.search_profile),

    path('profile/<int:id>', views.profile),
    path('profile_add/', views.profile_add),
    path('profile_edit/<int:id>/', views.profile_edit),
    path('profile_delete/<int:id>/', views.profile_delete),

    path('prescription/<int:id>', views.prescription),
    path('prescription_add/', views.prescription_add),
    path('prescription_edit/<int:id>', views.prescription_edit),
    path('prescription_delete/<int:id>', views.prescription_delete),
]
