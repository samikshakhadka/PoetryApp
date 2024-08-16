from rest_framework import routers

from .views import  PoemViewSet

router = routers.DefaultRouter()
router.register(r"", PoemViewSet,)
urlpatterns= router.urls