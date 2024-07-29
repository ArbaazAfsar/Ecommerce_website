from django.shortcuts import render


def cart_summery(request):
    return render(request, 'summery.html', {})



def cart_add(request):
    return render(request, 'add.html', {})



def cart_delete(request):
    return render(request, 'delete.html', {})
    


def cart_update(request):
    return render(request, 'update.html', {})
    

# Create your views here.
