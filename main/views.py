from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list": todo_list})

def second(request):
    return HttpResponse('test 2 page')

def third(request):
    return HttpResponse("This is page test3")

def first(request):
    return HttpResponse('Ваша запись была добавлена успешно')

def first1(request):
    return HttpResponse('Ваша запись была изменена успешно')

def first2(request):
    return HttpResponse('Ваша запись была удалена')

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)    

def marked_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)    

def unmarked_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)        

def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test) 