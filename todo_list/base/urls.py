from django.urls import path
from .views import tasklist,taskdetail,taskcreate,taskupdate, taskdelete,custom_loginview,registerpage
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('login/',custom_loginview.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'), name='logout'),
    path('register/',registerpage.as_view(),name='register'),
    path('',tasklist.as_view(), name='tasks'),
    path('task/<int:pk>/',taskdetail.as_view(), name='task'),
    path('create-task/',taskcreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',taskupdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/',taskdelete.as_view(), name='task-delete'),
]