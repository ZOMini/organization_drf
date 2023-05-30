from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'
v1_router = DefaultRouter()


# v1_router.register(r'users', views.CreateUserView, 'Users')
# v1_router.register('create_organization', views.CreateOrganization, 'Create Organization')
# v1_router.register('create_event', views.CreateEvent, 'Create Event')

urlpatterns = [
    path('create_organization/', views.CreateOrganization.as_view({'post': 'create'}), name='create_organization'),
    path('create_event/', views.CreateEvent.as_view({'post': 'create'}), name='create_event'),
    path('full_event_info/<event_id>/', views.FullEventInfo.as_view({'get': 'retrieve'}), name='full_event_info'),
    path('custom_event_info/', views.CustomEventInfo.as_view({'get': 'list'}), name='custom_event_info'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(v1_router.urls)),
]
