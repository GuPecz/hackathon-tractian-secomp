from . import views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve

from . import views

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path("integration/", include("integration.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
