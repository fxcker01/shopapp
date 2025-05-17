from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import os

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("main.urls")),

    # Для зображень товарів (медіа з бази)
    re_path(r'^pictures/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # Для зображень з public/img → dist/img (Vue)
    re_path(r'^img/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'frontend/dist/img')}),

    # Для Vue-скриптів і стилів
    re_path(r'^assets/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.BASE_DIR, 'frontend/dist/assets')}),

    # Для всіх інших SPA маршрутів
    re_path(r'^(?!api|admin|pictures|assets|img).*$', TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
