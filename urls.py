from django.urls import path
from . import views

urlpatterns = [
    path('', views.assignment_list, name="assignment_list"),
    path('create/', views.create_assignment, name="create_assignment"),
    path('<int:assignment_id>/submit/', views.submit_assignment, name="submit_assignment"),
    path('<int:assignment_id>/submissions/', views.view_submissions, name="view_submissions"),
    path('delete/<int:assignment_id>/', views.delete_assignment, name='delete_assignment'),

]
