from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/int:pk>/',views.TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvudelete/int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),

]
