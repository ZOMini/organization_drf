from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views as api_views

app_name = 'api'
v1_router = DefaultRouter()

urlpatterns = [
    path('create_organization/', api_views.CreateOrganization.as_view({'post': 'create'}), name='create_organization'),
    path('create_event/', api_views.CreateEvent.as_view({'post': 'create'}), name='create_event'),
    path('full_event_info/<event_id>/', api_views.FullEventInfo.as_view({'get': 'retrieve'}), name='full_event_info'),
    path('custom_event_info/', api_views.CustomEventInfo.as_view({'get': 'list'}), name='custom_event_info'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(v1_router.urls)),
]
