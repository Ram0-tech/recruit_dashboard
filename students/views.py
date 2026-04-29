from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    """
    List view for displaying all students, with an optional search filter
    based on course interest.
    """
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')
        if query:
            queryset = queryset.filter(course_interest__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class StudentCreateView(CreateView):
    """
    Create view for adding a new student to the dashboard.
    Leverages Django's built-in model form handling.
    """
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
