from django.urls import path
from Portal import views

urlpatterns = [
    path('', views.ListNews.as_view(), name='ListNews'),
    path('<int:pk>/', views.DetailNews.as_view(), name='DetailNews'),
    path('create/', views.CreateNews.as_view(), name='CreateNews'),
    path('update/<int:pk>', views.UpdateNews.as_view(), name='UpdateNews'),
    path('delete/<int:pk>', views.DeleteNews.as_view(), name='DeleteNews'),
    path('search/', views.PostListSearch, name='SearchNews')

]
