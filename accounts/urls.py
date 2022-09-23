from django.urls import path
from . import views
# 
app_name='account'
urlpatterns=[
    path('sign-up/',views.UserRegisterView.as_view(),name='sign-up'),
]