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

    # 👉 Правильна обробка медіа (фото товарів)
    re_path(r'^pictures/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT
    }),

    # 👉 Статичні ресурси Vue
    re_path(r'^img/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend/dist/img')
    }),
    re_path(r'^assets/(?P<path>.*)$', serve, {
        'document_root': os.path.join(settings.BASE_DIR, 'frontend/dist/assets')
    }),

    # 👉 SPA має бути останнім, і не перехоплювати інші шляхи
    re_path(r'^(?!api|admin|pictures|img|assets).*$', TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
