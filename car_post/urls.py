from django.urls import path
from .import views
urlpatterns = [
    path('details/<int:id>',views.detail_post_view, name='car_details'),
    path('buy/<int:id>/', views.buy_car, name='buy_car'),
    # path('proile/<int:id>/', views.buy_car, name='buy_car')

]
