from django.shortcuts import redirect, render, HttpResponse
from .models import Todo
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import io
from django.http import FileResponse



def index(request):
    alltodos = Todo.objects.all()
    if request.method == "POST":
        note = request.POST["todo"]
        if note != '':
            todo = Todo(title = note)
            todo.save()
    
    context = {
        "alltodos":alltodos

    }
    return render(request,'index.html', context)

def export(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    allTodos = Todo.objects.all()
    y = 800
    for todo in allTodos:
        isDone = '✔' if todo.isDone else '✖'
        p.drawString(50, y,  todo.title + '        ' + isDone)
        y -= 20
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='todos.pdf')


def deleteTodo(request, todoID):
    todo = Todo.objects.get(id=todoID)
    todo.delete()
    return redirect(index)

def toggleStatus(request):
    if request.method == 'POST':
        todoId = request.POST['id']
        todo = Todo.objects.get(id=todoId)
        todo.isDone = False if todo.isDone else True
        todo.save()
    return redirect(index)