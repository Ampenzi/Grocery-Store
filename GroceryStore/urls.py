from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url 
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('accounts.urls')),
    path('', home, name='home')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Taji Admin"
admin.site.site_title = "Taji Admin"
admin.site.index_title = "Taji Admin"