from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('policy/', include('policy.urls')),
    path('admin/', admin.site.urls),
]
