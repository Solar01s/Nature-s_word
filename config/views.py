from django.shortcuts import render, redirect

def main_view(request):
    return render(request, 'main.html')

def about_view(request):
    return render(request, 'about.html')
