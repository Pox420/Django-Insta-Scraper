from django.shortcuts import render
from .scraper import MyBot
import time


# Create your views here.
def index(request):
    return render(request, 'InstaProfileApp/index.html')


def profile(request):
    username = request.POST.get('username')
    # print(username)
    master_dict = MyBot(username)
    # print(master_dict)
    time.sleep(5)
    return render(request, 'InstaProfileApp/profile.html', {
        'user_profile_image': master_dict['user_profile_image'],
        'user_name': master_dict['user_name'],
        'posts': master_dict['posts'],
        'followers': master_dict['followers'],
        'following': master_dict['following'],
        'images_links': master_dict['images_links']
    })
