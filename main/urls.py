from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
import os

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("main.urls")),

    # Картинки товарів (медіа)
    re_path(r'^pictures/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),

    # Іконки з dist/img
    re_path(r'^img/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend/dist/img')
    }),

    # Vue: стилі та скрипти
    re_path(r'^assets/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend/dist/assets')
    }),

    # SPA маршрути (тільки якщо index.html існує!)
    re_path(r'^(?!admin|api|pictures|img|assets).*$', TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
