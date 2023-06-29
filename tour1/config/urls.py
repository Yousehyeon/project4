from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tour import views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),            # http://127.0.0.1:8000/admin
    path('', views.index, name='index'),        # http://127.0.0.1:8000
    path('tour/', include('tour.urls')),      # http://127.0.0.1:8000/board
    path('common2/', include('common2.urls')),  # # http://127.0.0.1:8000/common2
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)