from django.urls import path

from db_manager import views

app_name = 'db_manager'

urlpatterns = [
    path("db-manager", views.db_manager, name="db-manager"),
    path("db-upload", views.db_upload, name="db-upload"),
    path("db-download", views.db_download, name="db-download"),

]
