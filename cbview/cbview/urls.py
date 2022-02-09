from django.urls import include, path
from django.contrib import admin

"""
    Because we're using viewsets instead of views, we can automatically generate the URL conf for our API, 
    by simply registering the viewsets with a router class.
"""

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]