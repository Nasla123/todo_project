from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    # path('delete/<int:task_id>',views.delete,name='delete'),
    # path('update/<int:id>',views.update,name='update'),
    path('task',views.TaskListView.as_view(),name='taskList'),
    path('taskdetail/<int:pk>',views.TaskDetailView.as_view(),name='taskdetail'),
    path('taskupdate/<int:pk>', views.TaskUpdateView.as_view(), name='taskupdate'),
    path('taskdelete/<int:pk>', views.TaskDeleteView.as_view(), name='taskdelete'),

]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

