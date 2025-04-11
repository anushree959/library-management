from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # Book list view
    path('add/', views.add_book, name='add_book'),  # Add book view
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),  # Edit book view
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),  # Delete book view
]
