from django.urls import path
from . import views
# 
urlpatterns=[
    path('signup/',views.SignUpApi.as_view()),
    path('profile/',views.ProfileApi.as_view())
]