from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('doggy_daycare.urls')),

    # Include authentication-related URL patterns from 'django.contrib.auth'
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
