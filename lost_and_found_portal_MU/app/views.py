from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/basic/home.html')



def lostItems(request):
    return render(request, 'app/basic/lost.html')


def foundItems(request):
    return render(request, 'app/basic/found.html')