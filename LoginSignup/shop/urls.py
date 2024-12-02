from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('product_form/', views.render_product_form, name='product_form'),
    path('view_product/<int:product_id>/', views.view_product, name='view_product'),
]