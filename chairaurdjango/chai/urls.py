
from django.urls import path
from . import views

# localhost:8000/chai
# localhost:8000/chai/order
urlpatterns = [
    path('', views.all_chai, name='All_chai'),
    # path('chai/order', views.all_chai, name='order'),
    path('menu/', views.menu, name='menu'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
]