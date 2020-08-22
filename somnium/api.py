from rest_framework import routers

from user.views import UserViewSet


router = routers.DefaultRouter()

router.register(r'user', UserViewSet)

urlpatterns = router.urls
