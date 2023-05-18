from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from .views import CommentViewSet, GroupViewSet, PostViewSet, UserViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register('users', UserViewSet, basename='user')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/',
         auth_views.obtain_auth_token,
         name='api-token-auth'),
]
