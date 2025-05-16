from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    re_path(r'^pictures/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r"^(?!api|admin|pictures).*", TemplateView.as_view(template_name="index.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)