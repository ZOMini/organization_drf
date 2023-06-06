from django_filters import rest_framework as django_filters
from djoser.views import UserViewSet
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.filters import EventsFilters
from api.models import Event
from api.serializers import (
    EventSerializer,
    FullEventSerializer,
    OrganizationSerializer,
    RegistrationSerializer
)


class CreateUserView(UserViewSet):
    serializer_class = RegistrationSerializer


class CreateOrganization(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.AllowAny]  # либо [permissions.IsAuthenticated]

    
class CreateEvent(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]


class FullEventInfo(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = FullEventSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        event_id = int(self.kwargs.get('event_id'))
        return Event.objects.get(id=event_id)


class CustomEventInfo(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', ]
    filterset_class = EventsFilters
    pagination_class = LimitOffsetPagination
    queryset = Event.objects.all()
