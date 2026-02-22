from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # existing accounts URLs
    path('api/', include('posts.urls')),             # <-- add this line
]