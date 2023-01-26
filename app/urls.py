from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/<slug>', views.ItemDetailView.as_view(), name='product'),
    path('additem/<slug>', views.addItem, name='addItem'),
    path('subitem/<slug>', views.subItem, name='subItem'),
    path('removeitem/<slug>', views.removeItem, name='removeItem'),
    path('order/', views.OrderView.as_view(), name='order'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
]