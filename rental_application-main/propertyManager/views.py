from .serializers import CurrentUserPropertySerialzer
from . permissions import OwnerOrReadObly
from django.shortcuts import render, get_object_or_404
from rest_framework import mixins, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, APIView
from .serializers import ProperySerializer
from .models import PropertyDetail
# Create your views here.


class PropertyPostListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    permission_classes = [IsAuthenticated]
    serializer_class = ProperySerializer
    queryset = PropertyDetail.objects.all()

    def get(self, request:Request, pk=None):
        if pk:
            return self.retrieve(self, pk=pk)
        return self.list(request)
    
class ProperyPostView(generics.GenericAPIView):
    serializer_class =ProperySerializer
    queryset = PropertyDetail.objects.all()
    permission_classes = [IsAuthenticated]
    def post(self, request:Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            # serializer.owner = request.user
            serializer.save()
            response = {
                "message": "Propery Details Submitted Successfylly",
                "data": serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            response = {
                "message":serializer.errors
            }
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["GET"])
@permission_classes([IsAuthenticated, OwnerOrReadObly])
def get_properties_for_current_user(request: Request):
    user = request.user
    serializer = CurrentUserPropertySerialzer(
        instance=user, context={"request": request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)


class PropertyDeletePutApiView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ProperySerializer
    queryset = PropertyDetail.objects.all()
    permission_classes = [IsAuthenticated, OwnerOrReadObly]

    def put(self, request: Request, *args, **kwargs):
        permission_classes = [OwnerOrReadObly]
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        permission_classes=[OwnerOrReadObly]
        return self.destroy(request, *args, **kwargs)

