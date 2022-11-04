from django.shortcuts import render,redirect
from .models import List

# Create your views here.
def home(request):
    items = List.objects.all()
    context={
        "items":items
    }
    return render(request, 'home.html',context)

def add_item(request):
    return render(request, 'new.html')

def create_item(request):
    new_item = List(description=request.POST['description'])
    if new_item.description:
        new_item.save()
    return redirect('home')


def delete_item(request, pk):
    List.objects.get(id=pk).delete()
    return redirect('home')



