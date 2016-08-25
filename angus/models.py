from __future__ import unicode_literals

from django.contrib.gis.db import models as gis_model
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.



class GuestBook(models.Model):
    #content
    #pub-date
    #author (Foreign-key)
    #mod-date
    #pics
    content = models.TextField()
    author = models.CharField(max_length=120,default='Visitor')
    pub_date = models.DateTimeField('datetime',default=now())
    mod_date = models.DateTimeField('datetime',default=now())
    ip_address = models.GenericIPAddressField(blank=False,null=False)

    def __unicode__(self):
        return self.author +" : "+self.content



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
    picture = models.ImageField(upload_to='profile_image',blank=True)

    """
    Gender, Age, GPS,
    """
    def __unicode__(self):
        return self.user.username


