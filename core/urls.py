from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('detail/<int:pk>/',views.product_detail,name='detail'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.userlogout,name='logout'),
    path('login/',views.userlogin,name='login'),
    path('paymentsuccess/<int:pk>/',views.paymentsuccess,name='success'),
    path('paymentfailed/<int:pk>/',views.paymentfailed,name='failed'),
    path('search/',views.search,name='search'),
    path('like/<int:pk>',views.product_like,name='likes'),

]
