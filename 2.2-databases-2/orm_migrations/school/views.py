from django.views.generic import ListView
from django.shortcuts import render

from school.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'students'
    ordering = 'group'

    def get_queryset(self):
        return super().get_queryset().order_by(self.ordering)
