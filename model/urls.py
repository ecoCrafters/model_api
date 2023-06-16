from django.contrib import admin
from django.urls import path, include
from model_api import urls as model_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('models/', include(model_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)