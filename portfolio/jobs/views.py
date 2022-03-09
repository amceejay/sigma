from django.shortcuts import render

# Create your views here.
#creating the cajetan function

def cajetan(request):
    return render (request, 'jobs/home.html')