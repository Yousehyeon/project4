from django.contrib import admin
from django.urls import path, include
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000
    path('', views.index),
    path('board/', include('board.urls')),
    path('common2/', include('common2.urls')),
]
