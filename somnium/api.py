from rest_framework import routers

from user.views import UserViewSet
from group.views import GroupViewSet
from position.views import PositionViewSet
from profession.views import ProfessionViewSet


router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'group', GroupViewSet)
router.register(r'position', PositionViewSet)
router.register(r'profession', ProfessionViewSet)

urlpatterns = router.urls
