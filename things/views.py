from django.shortcuts import render, redirect
from .forms import ThingForm
from .models import Thing

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            pass
    else:
        form = ThingForm()
    return render(request, 'home.html', {'form': form})
