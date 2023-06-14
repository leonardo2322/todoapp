from django.urls import path
from . import views
urlpatterns = [
    path('',views.signup),
    path('home/',views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/',views.tasks, name='tasks'),
    path('tasks_completed/',views.completed_task, name='tasks_completed'),
    path('logout/', views.signout, name='logout'),
    path('signin/',views.signin, name='signin'),
    path('create/task/', views.create_Task, name='create_task'),
    path('tasks/<int:task_id>/complete_task',views.complete, name='complete_task'),
    path('tasks/<int:task_id>/',views.TaskDetail, name='taskdetail'),
    path('tasks/<int:task_id>/delete',views.delete_task, name='deletetask')
    
]
