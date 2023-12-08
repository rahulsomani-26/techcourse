
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', include('accounts.urls')),
    path('signout/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
]
