from django.shortcuts import render, get_object_or_404, redirect
from .models import Shoe
from .forms import ShoeForm

def shoe_list(request):
    shoes = Shoe.objects.all()
    return render(request, 'api/shoe_list.html', {'shoes': shoes})

def shoe_detail(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    return render(request, 'api/shoe_detail.html', {'shoe': shoe})

def shoe_create(request):
    if request.method == "POST":
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shoe_list')
    else:
        form = ShoeForm()
    return render(request, 'api/shoe_create.html', {'form': form})

def shoe_update(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    if request.method == "POST":
        form = ShoeForm(request.POST, instance=shoe)
        if form.is_valid():
            form.save()
            return redirect('shoe_detail', pk=shoe.pk)
    else:
        form = ShoeForm(instance=shoe)
    return render(request, 'api/shoe_update.html', {'form': form})
