from django.contrib import admin
from django.urls import path,include
# jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('',include('song.urls')),
    path('',include('accounts.urls')),

    # APIs
    path('api/',include('home.api.urls')),
    path('api/song/',include('song.api.urls')),
    path('api/',include('accounts.api.urls')),


    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
