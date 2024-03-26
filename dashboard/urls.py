from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('notes',views.notes,name="notes"),
    path('delete_note/<int:pk>',views.delete_note,name="delete_note"),
    path('note_detail/<int:pk>',views.NotesDetailView.as_view(),name="notes-detail"),     #pk = primary key
    path('homework',views.homework,name="homework"),
    

    
]