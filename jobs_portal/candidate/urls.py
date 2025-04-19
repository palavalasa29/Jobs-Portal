from django.urls import path
from candidate import views 
from authuser import views as authviews

urlpatterns = [
    path('candidate-dashboard/', views.candidate_dashboard, name="candidate_dashboard"),
    path('logout/', authviews.logout_user, name="logout"), #have to check why it is not working 
    path('joblist/', views.jobList, name = "joblist"),
    path('apply-job/<int:jobId>/', views.apply, name = "apply_job"),

]