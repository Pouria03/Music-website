from django.urls import path
from . import views
# 
app_name='accounts'
urlpatterns=[
    path('signup/',views.UserRegisterView.as_view(),name='signup'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('get-pro/',views.GetPremiumView.as_view(),name='get-pro'),
    path('profile/',views.ProfileView.as_view(),name='profile')


]