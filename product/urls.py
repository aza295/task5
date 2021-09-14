from django.urls import path
from product.views import ProductListView, ProductDetailView, CreateProductView, UpdateProductView, DeleteProductView, \
    ProductViewSet

urlpatterns = [
    path('find/',ProductListView.as_view()),
    path('find/<int:pk>/',ProductDetailView.as_view()),
    path('make/create/',CreateProductView.as_view()),
    path('new/update/<int:pk>', UpdateProductView.as_view()),
    path('del/delete/<int:pk>', DeleteProductView.as_view())

]


urlpatterns = [
    path('find/', ProductViewSet.as_view(
        {'get': 'list',
         'post': 'create'}
    )),
    path('new/', ProductViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy'}
    )),
]


