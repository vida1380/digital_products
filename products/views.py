
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated



from .models import Category, Products, File
from .serializers import CategorySerializer, ProductSerializer, FileSerializer



class CategoryListView(APIView):


    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True,  context={'request': request})
        return Response(serializer.data)


class CategoryDetailView(APIView):

    def get(self, request, pk):
        try:
            category = Category.object.get(pk=pk)

        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data)





class ProductListView(APIView):



    def get(self, request):
        # print(request.user)
        # print(request.auth)

        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True,  context={'request': request})
        return Response(serializer.data)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            product = Products.object.get(pk=pk)

        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)






class FileListView(APIView):


    def get(self, request, product_id):
        files = File.objects.filter(product_id=product_id)
        serializer = FileSerializer(files, many=True,  context={'request': request})
        return Response(serializer.data)


class FileDetailView(APIView):

    def get(self, request, product_id, pk):
        try:
            f = File.objects.get(pk=pk, product_id=product_id)

        except Products.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FileSerializer(f, context={'request': request})
        return Response(serializer.data)