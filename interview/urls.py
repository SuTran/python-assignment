from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from rest.views import PersonDetailUpdateAPIView, PersonListCreateAPIView

router = routers.DefaultRouter()
router.register(r'users', PersonDetailUpdateAPIView)
router.register(r'users', PersonListCreateAPIView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
