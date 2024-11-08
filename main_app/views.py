from django.shortcuts import render, redirect, get_object_or_404
from .models import Practice, Registration
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def home(request):
    return render(request, 'main_app/home.html')

def practice_list(request):
    practices = Practice.objects.filter(is_closed=False)
    return render(request, 'main_app/practice_list.html', {'practices': practices})

@login_required
def register_practice(request, pk):
    practice = get_object_or_404(Practice, pk=pk)
    if Registration.objects.filter(practice=practice).count() >= practice.max_participants:
        practice.is_closed = True
        practice.save()
        return redirect('main_app:practice_list')
    Registration.objects.create(user=request.user, practice=practice)
    return redirect('main_app:practice_list')
