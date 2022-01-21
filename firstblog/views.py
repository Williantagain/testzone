from django.shortcuts import render
def post_list(request):
 return render(request, 'firstblog/post_list.html', {})