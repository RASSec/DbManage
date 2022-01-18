from django.shortcuts import render

# Create your views here.

def index(request):
    username = request.GET.get('username')
    return render(request, 'main/index.html',context={'username':username})