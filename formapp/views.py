from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.http import JsonResponse
from .models import Branch

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Application accepted"
            return render(request, 'success.html', {'message': message})
    else:
        form = RegistrationForm()
    
    return render(request, 'registration_form.html', {'form': form})

def home_view(request):
    return render(request, 'index.html')


def get_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).values('id', 'name')
    return JsonResponse(list(branches), safe=False)
