from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('student/', views.studentData, name="task-filter"),
	path('senior', views.shapiOverview, name="shapi-overview"),
	path('senior/student/', views.shstudentData, name="shtask-filter"),
	path('studentPush/', views.studentPush, name="student-push"),
]
