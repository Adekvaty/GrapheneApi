from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from main.views import BrandViewSet, ClothesViewSet

from django.contrib import admin
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Brands Rest API",
        default_version='v1',
        description="Этот хорошо структурированный REST API позволяет вам управлять запасами воздушных шаров, ценообразованием и потенциальными контактами с клиентами в рамках бизнеса воздушных шаров или связанного с ним приложения. Он предлагает полный набор конечных точек для операций CRUD (создание, чтение, обновление, удаление) на различных ресурсах, связанных с balloon, обеспечивая гибкость и контроль над вашими данными.",
        terms_of_service="https://policies.google.com/",
        contact=openapi.Contact(
            name="Ilyas",
            url="https://t.me/the_ilyas",
            email="thegg2022@gmail.com",
            ),
            license=openapi.License(
                name="MIT",
                url="https://opensource.org/license/mit"
            ),
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser]
)


router = DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'clothes', ClothesViewSet)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns += router.urls