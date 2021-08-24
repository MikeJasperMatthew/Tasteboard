from rest_framework import routers
from .api import BoardViewSet

router = routers.DefaultRouter()
router.register('api/boards', BoardViewSet, 'boards')

urlpatterns = router.urls