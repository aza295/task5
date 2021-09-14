from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializer import ProductListSerializer

@api_view(['GET'])
def product(request):
    prod = Product.objects.only('title')
    serializer = ProductListSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def product_detail(request, pk):
    prod = Product.objects.get(id=pk)
    serializer = ProductListSerializer(prod, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    prod = Product.objects.all()
    serializer = ProductListSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def update_product(request):
    prod = Product.objects.all()
    serializer = ProductListSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])
def update_product_patch(request):
    prod = Product.objects.all()
    serializer = ProductListSerializer(prod, many=True)
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_product(request):
    prod = Product.objects.all()
    serializer = ProductListSerializer(prod, many=False)
    return Response(serializer.data)


class ProductListView(ListAPIView):
    queryset = Product.objects.only('title')
    serializer_class = ProductListSerializer


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class UpdateProductView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductListSerializer
        return ProductListSerializer
@api_view(['GET'])
def all_list(request):
    pubs = Product.objects.all()
    serializer = ProductListSerializer(pubs, many=True)
    return Response(serializer.data)  # Response возвращает http ответ


@api_view(['GET'])
def detail(request, pk):
    pubs = Product.objects.get(id=pk)
    serializer = ProductListSerializer(pubs, many=False)
    return Response(serializer.data)  # Response возвращает http ответ


@api_view(['POST'])
def create_view(request):
    serializer = ProductListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Response в


@api_view(['PUT'])
def patch_product(request):
    pubs = Product.objects.all()
    serializer = ProductListSerializer(pubs, many=True)
    return Response(serializer.data)  # Response возвращает http ответ


@api_view(['DELETE'])
def delete_product(request, pk):
    pubs = Product.objects.get(id=pk)
    pubs.delete()
    return Response("Successfully deleted", status=status.HTTP_204_NO_CONTENT)  # Resp


@api_view(['UPDATE'])
def update_product(request, pk):
    pubs = Product.objects.get(id=pk)
    serializer = ProductListSerializer(instance=pubs, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  # Response возвращает http ответ


