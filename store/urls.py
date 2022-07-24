from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all products'),
    path('product/<slug:slug>', views.product_detail_page,
         name='product_detail_page'),
    path('search/<slug:category_slug>',
         views.category_list,  name="category_list")

]
