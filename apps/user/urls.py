from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import RegisterView, VerifyEmail, LoginView, LogoutView, ChangePasswordView

router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/<uuid:verification_token>/', VerifyEmail.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('', include(router.urls)),
]
