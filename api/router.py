from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'test', views.testViewSet, basename='test')
