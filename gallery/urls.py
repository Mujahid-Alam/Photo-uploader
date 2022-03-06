
from django.contrib import admin
from django.urls import path
from album.views import home

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="homepage"),
] + static(settings.MEDIA_URL, documents_root = settings.MEDIA_ROOT)
