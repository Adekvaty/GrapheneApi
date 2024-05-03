
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', include('grapheneapi.urls')),
    path('api/', include('main.urls'))
]


