from django.urls import path
from .views import index,client_home,client_create,client_remove,product_create,product_home,product_remove,product_catalog

urlpatterns = [
   path('',index,name='index') ,
   path('client',client_home,name='client.home') ,
   path('client/create',client_create,name='client.create') ,
   path('client/<int:id>/delete',client_remove,name='client.delete'),
   path('client/<int:id>/edit',client_create,name='client.edit'),
   path('product',product_home,name='product.home') ,
   path('product/create',product_create,name='product.create') ,
   path('product/<int:id>/delete',product_remove,name='product.delete'),
   path('product/<int:id>/edit',product_create,name='product.edit'),
   path('product/catalog',product_catalog,name='product.catalog')
]
