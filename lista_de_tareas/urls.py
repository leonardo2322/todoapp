from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup),
    path('home/',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/',views.tasks, name='tasks'),
    path('logout/', views.signout, name='logout'),
    path('signin/',views.signin, name='signin')
]
