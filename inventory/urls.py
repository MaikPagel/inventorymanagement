from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('my_inventory')),
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
