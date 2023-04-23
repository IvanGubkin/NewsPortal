from django.urls import path
from Accounts import views
urlpatterns = [
    path('profile/', views.UserProfile, name='ProfileUser'),
    path('updateauthoruser/', views.UpdateUserAuthor, name='UpdateUserAuthor')
]
