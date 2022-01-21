from django.shortcuts import render
from django.utils import timezone
from .models import Firstblog

def post_list(request):
    firstblogs = Firstblog.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'firstblog/post_list.html', {'firstblogs': firstblogs})