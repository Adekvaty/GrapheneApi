from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from main.views import BrandViewSet, ClothesViewSet, PersonViewSet, CarViewSet

from django.contrib import admin
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='GRAPANE API',
        default_version='v1',
        description='GRAPANE API',
        terms_of_service="https://policies.google.com/",
        contact=openapi.Contact(
            name="Mereke",
            url = "https://t.me/merekeeh",
            email="merekeserik5@gmail.com",
            ),
            license=openapi.License(
                name="MIT License",
                url="https://opensource.org/license/mit",
            ),
        ),
        public=True,
        permission_classes=[permissions.IsAdminUser]
)




router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'clothes', ClothesViewSet)
router.register(r'persons', PersonViewSet)
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]