

from django.urls import path


from .views import (
    ProductListView, ProductDetailView, CategoryListView, CategoryDetailView,
    FileListView, FileDetailView,
)




urlpatterns = [

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),

    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products-detail'),

    path('products/<int:product_id>/files/', FileListView.as_view(), name='file_list'),
    path('products/<int:product_id>/files/<int:pk>/', FileDetailView.as_view(), name='file_detail')

]

