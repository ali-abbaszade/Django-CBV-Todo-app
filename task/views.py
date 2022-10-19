from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Task

class TaskList(ListView):
    model = Task    
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description', 'complete']    
    success_url = reverse_lazy('tasks')   

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']   
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')    