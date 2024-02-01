from django.contrib import admin
from django.urls import include, path

from landing import views as landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', landing.home)
]
