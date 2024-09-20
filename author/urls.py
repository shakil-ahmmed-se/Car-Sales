from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/',views.user_logout, name='user_logout'),
    path('profile/',views.profile, name='profile'),
    # path('buy/<int:id>/', views.buy_car, name='buy_car'),
    path('profile/edit',views.edit_profile, name='edit_profile'),
 
]
