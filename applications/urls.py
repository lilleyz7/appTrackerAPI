from django.urls import path
from .views import create_application_view, get_all_applications_view, get_application_by_id_view, delete_application_view, update_application_view

urlpatterns = [
    path("/add_app", create_application_view, name="create_application"),
    path("/get_apps", get_all_applications_view, name="get_all_apps"),
    path("/get_single_app/<int:pk>", get_application_by_id_view, name="get_single_app"),
    path("/update_app/<int:pk>", update_application_view, name="update_application"),
    path("/delete_app/<int:pk>", delete_application_view, name="delete_application"),
]
