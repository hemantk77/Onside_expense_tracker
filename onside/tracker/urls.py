from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('signup/', views.signup_view, name='signup'),
    path('transaction/new/', views.transaction_create_view, name='transaction_create'),
    path('transaction/<int:pk>/edit/', views.transaction_update_view, name='transaction_update'),
    path('transaction/<int:pk>/delete/', views.transaction_delete_view, name='transaction_delete'),
]