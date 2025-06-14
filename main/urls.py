from rest_framework.routers import SimpleRouter
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import ItemsPage, OrderAdd, ItemDetail
from .views_auth import register, login_view, user_profile
from rest_framework_simplejwt.views import TokenRefreshView

router = SimpleRouter()
router.register(r'items', ItemsPage)

urlpatterns = router.urls + [  # Додано router.urls сюди
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', user_profile, name='profile'),
    path('item/<slug:slug>/', ItemDetail.as_view(), name='item-detail'),
    path('order-add/', OrderAdd.as_view(), name='order_add'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
