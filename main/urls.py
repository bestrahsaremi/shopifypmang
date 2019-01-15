from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('show/', views.ProductListView.as_view(), name='product_list' ),
    path('create/', views.ProductCreateView.as_view(), name='product_add'),
]