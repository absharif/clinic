from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('website/', include('website.urls')),
    path('clinic/', include('chamber.urls')),
    path('', admin.site.urls),
]
