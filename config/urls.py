
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main'),
    path('accounts/', include('accounts.urls')),
    path('nature_index/', include('nature_index.urls')),
    path('about/', views.about_view, name='about'),
]
