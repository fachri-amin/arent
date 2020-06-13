from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import Home, redirectKeHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mitra/', include('mitra.urls', namespace='mitra')),
    path('', redirectKeHome, name='redirectKeHome'),
    path('page/<int:page>', Home.as_view(), name='home')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
