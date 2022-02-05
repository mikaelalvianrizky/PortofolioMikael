from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Todo

# Create your views here.
def index(request):
    items = Todo.objects.all()
    count = items.count()
    return render(request, 'todo/index.html', {'items': items, 'count':count})

def done(request):
    items = Todo.objects.filter(status=True)
    count = items.count()
    return render(request, 'todo/index.html', {'items': items, 'count':count})

def pending(request):
    items = Todo.objects.filter(status=False)
    count = items.count()
    return render(request, 'todo/index.html', {'items': items, 'count':count})

def delete_all(request):
    Todo.objects.all().delete()
    return HttpResponseRedirect(reverse('todo:index'))

def create(request):
    try:
        title = request.POST['title']
        Todo(title=title).save()
        return HttpResponseRedirect(reverse('todo:index'))
    except Exception:
        return HttpResponseRedirect(reverse('todo:index'))

def update(request, id):
    try:
        item = Todo.objects.get(id=id)
        item.status = not item.status
        item.save()
        return HttpResponseRedirect(reverse('todo:index'))
    except Exception:
        return HttpResponseRedirect(reverse('todo:index'))

def delete(request, id):
    try:
        Todo.objects.get(id=id).delete()
        return HttpResponseRedirect(reverse('todo:index'))
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('todo:index'))