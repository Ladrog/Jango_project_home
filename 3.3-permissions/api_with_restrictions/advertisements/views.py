from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from .models import Advertisement
from .serializers import AdvertisementSerializer


class AdvertisementFilter(filters.FilterSet):
    """Фильтр для объявлений"""
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']


class IsOwnerPermission(IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user


class AdvertisementViewSet(viewsets.ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        return []

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise PermissionError("Вы не можете удалить это объявление.")
        instance.delete()
