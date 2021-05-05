from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostView.as_view(), name='blog_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='blog_detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='blog_results'),
]