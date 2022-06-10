from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('search_profile/', views.search_profile, name='search_profile'),

    path('profile/<int:id>/', views.profile, name='profile'),
    path('profile_add/', views.profile_add, name='profile_add'),
    path('profile_edit/<int:id>/', views.profile_edit, name='profile_edit'),
    path('profile_delete/<int:id>/', views.profile_delete, name='profile_delete'),
    path('profile_delete_confirm/<int:id>/', views.profile_delete_confirm, name='profile_delete_confirm'),

    path('prescription/<int:id>/', views.prescription),
    path('prescription_add/<int:profile_id>/', views.prescription_add, name='prescription_add'),
    path('prescription_edit/<int:profile_id>/<int:id>/', views.prescription_edit, name='prescription_edit'),
    path('prescription_delete/<int:profile_id>/<int:id>/', views.prescription_delete, name='prescription_delete'),
    path('prescription_confirm_delete/<int:profile_id>/<int:id>/', views.prescription_confirm_delete, name='prescription_confirm_delete'),

]
