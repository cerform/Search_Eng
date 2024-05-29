from . import views
from django.contrib import admin
from django.urls import path, include
from app.authentication import CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    path('documents/', views.DocumentListView.as_view(), name='document-list'),
    path('documents/upload/', views.DocumentUploadView.as_view(), name='document-upload'),
    path('documents/<int:pk>/', views.DocumentDetailView.as_view(), name='document-detail'),
]
