
from django.contrib import admin
from django.urls import path,include
import app_test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('app_test.urls')),
]
