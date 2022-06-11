from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('website.urls')),  # This will be blank url
    path('clinic/', include('chamber.urls')),
    path('admin/', admin.site.urls, name='admin'),
]
