
from django.shortcuts import render
from webapp.cat import Cat

def stats_view(request):
    if request.POST.get('action') == 'play':
        Cat.play()
    elif request.POST.get('action') == 'feed':
        Cat.feed()
    elif request.POST.get('action') == 'sleep':
        Cat.get_sleep()
    context = {
        'image': Cat.set_img(),
        'name': Cat.name,
        'age': Cat.age,
        'mood': Cat.mood,
        'satiety': Cat.satiety
    }
    return render(request, 'cat_stats.html',context=context)