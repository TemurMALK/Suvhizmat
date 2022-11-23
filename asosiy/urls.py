from django.contrib import admin
from django.urls import path
from water.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Suvhizmat",
      default_version='v1',
      description="Bu loyiha Suv haqida",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="jalalovtemurmalik561@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('suvlar/', SuvlarAPIView.as_view()),
    path('suv/<int:pk>/', SuvAPIView.as_view()),
    path('mijozlar/', MijozlarAPIView.as_view()),
    path('mijoz/<int:pk>/', MijozAPIView.as_view()),
    path('buyurtmalar/', BuyurtmalarAPIView.as_view()),

    path('buyurtma/<int:pk>/', BuyurtmaAPIView.as_view()),
    path('haydovchilar/', HaydovchilarAPIView.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiAPIView.as_view()),
    path('get_token/', TokenObtainPairView.as_view()),
    path('token_yangila/', TokenRefreshView.as_view()),
    path('docs/', schema_view.with_ui("swagger",cache_timeout=0))
]
