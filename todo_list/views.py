from django.shortcuts import render, redirect
from .forms import todoform
from .models import todo
from django.views.decorators.http import require_POST

def index(request):
	mytodo = todo.objects.order_by('id')
	form =  todoform()
	context = { 'mytodo': mytodo , 'form': form }
	return render(request, 'todo_list/index.html', context)

@require_POST
def newTodo(request):
	form = todoform(request.POST)

	if form.is_valid():
		mynew = todo(todotext=request.POST['text'])
		mynew.save()

	return redirect('index')

def completeTodo(request, todo_id):
	mytodo = todo.objects.get(pk=todo_id)
	mytodo.complete = True 
	mytodo.save()

	return redirect('index')

def deleteTodo(request):
	todo.objects.filter(complete__exact=True).delete()

	return redirect('index')