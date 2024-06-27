from django.urls import path

from school.views import StudentListView

urlpatterns = [
    path('students/', StudentListView.as_view(), name='students_list'),
]
