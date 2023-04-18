from django.urls import path
from Portal import views

urlpatterns = [
    path('', views.ListNews.as_view(), name='ListNews'),
    path('<int:pk>/', views.DetailNews.as_view(), name='DetailNews'),

]
