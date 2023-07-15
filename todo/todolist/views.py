from django.shortcuts import render
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todolist/main_page.html', {'todo_list': todos, 'title': 'Главная страница'})
