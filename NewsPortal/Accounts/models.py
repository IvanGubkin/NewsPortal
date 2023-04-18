from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=0)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)

    def update_rating(self):
        pos = self.post_set.aggregate(postRat=Sum('rating'))
        posR = 0
        posR += pos.get('postRat')

        com = self.authorUser.comment_set.aggregate(comSum=Sum('rating'))
        comR = 0
        comR += com.get('comSum')

        self.rating = posR + comR
        self.save()

    def __str__(self):
        return f'{self.name}'
