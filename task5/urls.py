"""task5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
#
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('product/', include('product.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#


from django.urls import path

from product.views import *

urlpatterns = [
    path('product/func/', product),
    path('product/func/detail/<int:pk>/', product_detail),
    path('product/func/create/', create_product),
    path('product/func/update/', update_product),
    path('product/func/patch/', update_product_patch),
    path('product/func/delete/', delete_product),

    path('product/', ProductListView.as_view()),
    path('product/detail/<int:pk>/', ProductDetailView.as_view()),
    path('product/create/', CreateProductView.as_view()),
    path('product/update/', UpdateProductView.as_view()),
    path('product/delete/', DeleteProductView.as_view()),

    path('prod/', ProductViewSet.as_view({'get': 'list',
                                          'post': 'create'})),
    path('prod/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve',
                                                   'put': 'update',
                                                   'patch': 'partial_update',
                                                   'delete': 'destroy'})),



    path('prods/', ProductListsView.as_view()),
    path('prods/details/<int:pk>/', ProductDetailsView.as_view()),
    path('prods/create/', CreatesProductView.as_view()),
    path('prods/update/', UpdatesProductView.as_view()),
]