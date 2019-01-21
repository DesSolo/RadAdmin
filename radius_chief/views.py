from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from . import serializers
from . import models


class RadPostAuthListView(generics.ListAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.RadPostAuth.objects.all().order_by('-id')
    serializer_class = serializers.RadPostAuthSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username', 'reply', 'authdate')


class RadCheckListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.RadCheck.objects.all().order_by('-id')
    serializer_class = serializers.RadCheckSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)


class RadCheckUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.RadCheck.objects.all()
    serializer_class = serializers.RadCheckSerializer


class RadUserGroupListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.RadUserGroup.objects.all()
    serializer_class = serializers.RadUserGroupSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)


class RadUserGroupUpdateDestroyCreateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = models.RadUserGroup.objects.all()
    serializer_class = serializers.RadUserGroupSerializer


