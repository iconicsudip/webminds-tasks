from django.urls import path
from ft import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('addexpenses',views.expenses,name='add_expenses'),
    path('visualize',views.visualize,name='visualize')
]
