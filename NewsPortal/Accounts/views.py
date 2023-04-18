from django.shortcuts import render


def UserProfile(request):
    context = request.user
    return render(request, 'accounts/ProfileUser.html', {'context': context})
