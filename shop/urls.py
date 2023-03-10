from django.urls import path
from . import views # importing views module from current folder

app_name = "shop"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatDetails')
]