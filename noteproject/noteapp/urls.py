from django.urls import path
from . import views

urlpatterns=[
   path('signup/', views.registerPage, name='sign_up'),
   path('', views.home, name='home'),
   path('note/', views.notes, name='notes'),
   
   path('pinned_note/', views.pinned_note, name='pinned_note'),
   path('category/', views.category_list, name='category'),
   path('category-note/<int:pk>', views.category_note, name='category_note'),
   path('profile/', views.profile, name='my_profile'),
   path('user_update/', views.userupdate, name='user_update'),
   
   path('note_create/', views.note_create, name='note_create'),
   path('note_update/<int:pk>/', views.note_update, name='note_update'),
   
   path('note_delete/<int:pk>/', views.note_delete, name='note_delete'),
   path('note_restore/<int:pk>/', views.restore_note, name='note_restore'),
   path('delete_note_perm/<int:pk>/', views.delete_note, name='delete_note_perm'),
   path('trash_note/', views.trash_notes, name='trashed_note'),
   path('detail_note/<int:pk>', views.detail_notes, name="detail_note"),
   path('share_note/', views.share_note, name='share_note'),

]



