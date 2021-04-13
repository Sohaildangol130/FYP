from django.urls import path
from .views import view_post, upload_post, edit_post, delete_post
urlpatterns = [
    path('upload', upload_post),
    path('<int:id>', view_post),
    path('edit/<int:id>', edit_post),
    path('delete/<int:id>', delete_post)
]