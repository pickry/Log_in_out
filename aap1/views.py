from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html', {'title' : 'Django', 'link':'http://127.0.0.1:8000/'})

def profile(request):
    return render(request, 'profile.html', {'title' : 'Django','link':'http://127.0.0.1:8000/'})

def expression(request):
    #was earlier GET secured with POST
    a = int(request.POST['text1'])
    b = int(request.POST['text2'])
    c = a*2 + b
    return render(request, 'output.html' , {'answer' : c, 'link' : 'http://127.0.0.1:8000/'})