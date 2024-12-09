from django.urls import path, include
from .router import router
urlpatterns = [
    #router instead
    path('', include(router.urls)),
]
