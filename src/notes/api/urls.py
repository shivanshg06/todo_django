from django.urls import path
from .views import getRoutes, getNotes, createNote, getNote, updateNote, deleteNote

urlpatterns = [
    path('', getRoutes),
    path('notes/', getNotes),
    path('notes/create/', createNote),
    path('notes/<str:pk>/update/', updateNote),
    path('notes/<str:pk>/delete/', deleteNote),
    path('notes/<str:pk>/', getNote),
]