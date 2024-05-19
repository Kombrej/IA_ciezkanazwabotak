from django.shortcuts import render
from .models import Staff
# Create your views here.
def home(request):
    WorkTimehoursT= Staff.objects.all()
    return render(request, 'WorkTime/home.html', {'WorkTimehoursT': WorkTimehoursT})
def base(request):
    return render(request, 'WorkTime/base.html', {})