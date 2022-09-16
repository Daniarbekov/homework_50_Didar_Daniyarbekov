from django.shortcuts import render, redirect
from webapp.cat import Cat


def index_view(request):
    Cat.name = request.POST.get('cat_name')
    if Cat.name:
        return redirect('/cat_stats')
    return render(request, 'home.html')