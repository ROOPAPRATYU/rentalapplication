from django.urls import path
from .views import PropertyPostListView, ProperyPostView,PropertyDeletePutApiView, get_properties_for_current_user

urlpatterns = [
    path('list/', PropertyPostListView.as_view(), name="propertyList"),
    path('list/<int:pk>', PropertyPostListView.as_view(), name="property"),

    path('post_property/', ProperyPostView.as_view(), name="post_property"),
    path("user_property/", get_properties_for_current_user, name="usersProperty"),
    path("user_property/<int:pk>", PropertyDeletePutApiView.as_view(), name="property_details")
]
