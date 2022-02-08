from django.urls import include, path
from rest_framework import routers
from tutii.qs import views

"""
    Because we're using viewsets instead of views, we can automatically generate the URL conf for our API, 
    by simply registering the viewsets with a router class.
"""

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]