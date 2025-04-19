from django.urls import path
from hr import views


urlpatterns = [
    path('hrdashboard/', views.hrHome, name = "hrHome"),
    path('post-job/', views.post_job, name = "post_job"),
    path('candidate-details/<int:id>/', views.candidate_view, name = "candidate_details"),
    path('select-candidate/', views.selectCandidate, name = "selectCandidate"),
    path('delete-candidate/', views.deleteCandidate, name = "deleteCandidate"),
]