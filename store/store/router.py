from rest_framework import routers
from api import views as api_views

router = routers.DefaultRouter()
router.register('product', api_views.ProductViewSet)
router.register('order', api_views.OrderViewSet)
