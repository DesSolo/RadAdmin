from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api-v1/', include('radius_chief.urls')),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]
