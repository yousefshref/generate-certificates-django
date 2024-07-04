from django.contrib import admin
from django.urls import path

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/signup/', views.signup),
    path('api/login/', views.login),

    path('api/user/', views.user_detail),

    path('api/certificates/', views.certificates_list),
    path('api/certificates/<int:pk>/', views.certificate_detail),
]
