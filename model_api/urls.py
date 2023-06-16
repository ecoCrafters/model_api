from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from .views import (
    TodoListApiView,
    # TodoDetailApiView
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    # path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)