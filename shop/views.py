from django.shortcuts import render

def mainscreen(request):
    return render(request, 'titlemenu.html')
