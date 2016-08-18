from __future__ import unicode_literals

from django.contrib.gis.db import models as gis_model
from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import
#from django.contrib.auth import models.User

# Create your models here.
#class PUser(models.)
class UserProfile(models.Model):
    BRONZE = 'BR'
    SILVER = 'SL'
    GOLD = 'GL'
    PLATINUM = 'PL'
    DIAMOND = 'DI'
    MASTER = 'MA'
    CHALLENGER = 'CH'

    GRADE_CHOICES = (
        (BRONZE, 'Bronze'),
        (SILVER, 'Silver'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
        (DIAMOND, 'Diamond'),
        (MASTER, 'Master'),
        (CHALLENGER, 'Challenger'),
    )
    grade = models.CharField(max_length=120, default=BRONZE, choices=GRADE_CHOICES)
    user = models.OneToOneField(User)
    #picture = models.ImageField(upload_to='profile_image',blank=True)

    """
    Gender, Age, GPS,
    """
    def __unicode__(self):
        return self.user.username

class User(models.Model):
    BRONZE='BR'
    SILVER='SL'
    GOLD='GL'
    PLATINUM='PL'
    DIAMOND='DI'
    MASTER='MA'
    CHALLENGER='CH'

    GRADE_CHOICES = (
        (BRONZE,'Bronze'),
        (SILVER,'Silver'),
        (GOLD,'Gold'),
        (PLATINUM,'Platinum'),
        (DIAMOND,'Diamond'),
        (MASTER,'Master'),
        (CHALLENGER,'Challenger'),
    )

    user_id = models.CharField(max_length=12,primary_key=True) #need to limit range of character
    password = models.CharField(max_length=8) #need to define minimum length
    e_mail = models.EmailField(max_length=128)
    grade = models.CharField(max_length=120,default=BRONZE,choices=GRADE_CHOICES)
    registration_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'fuck you'



