from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .models import Author


def UserProfile(request):
    context = request.user
    return render(request, 'accounts/ProfileUser.html', {'context': context})


def UpdateUserAuthor(request):
    user = request.user
    group = Group.objects.get(name='authors')
    if not user.groups.filter(name='authors').exists():
        group.user_set.add(user)
    Author.objects.create(name=User.objects.get(pk=user.id))
    massage = 'Поздравляем теперь вы можете писать статьи!'
    return render(request, 'accounts/UpdateUserAuthor.html', {'massage': massage})

