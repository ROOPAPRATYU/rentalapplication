from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import TenetRegisterView, TenetListView, OwnerListView, LoginView, OwnerRegisterView, User_logout

urlpatterns = [
    path('tenet_registration/', TenetRegisterView.as_view(), name="tenet-register"),
    path('tenet_list/', TenetListView.as_view(), name="tenet-list"),
    path('owner_registration/', OwnerRegisterView.as_view(), name="owner-register"),
    path('owner_list/', OwnerListView.as_view(), name="owner-list"),
    path('login/', LoginView.as_view(), name="login_page"),
    path('logout/', User_logout.as_view(), name="logout"),
    # path('current_user/', CurrentUserProfile.as_view(), name='currentUser'),



    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),



    # for Propery Details
]
