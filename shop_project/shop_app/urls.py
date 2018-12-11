from django.urls import path
from . import views

app_name = 'shop_app'

urlpatterns = [
  path('', views.index, name='index'),
  path('products/<int:product_id>', views.product, name='product'),
]