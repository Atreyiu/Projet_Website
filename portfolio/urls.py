from django.urls import path

from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.PortfolioView.as_view(), name='portfolio_index'),
    path('<int:pk>/', views.DetailView.as_view(), name='portfolio_detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='portfolio_results'),
]