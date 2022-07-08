# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.db import models
from django.db.models import SET_NULL


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, SET_NULL, null=True, blank=True,
                                   related_name='created_%(model_name)ss')
    updated_by = models.ForeignKey(User, SET_NULL, null=True, blank=True,
                                   related_name='updated_%(model_name)ss')

    class Meta:
        abstract = True


class Room(BaseModel):
    number = models.IntegerField(null=True)
    image = models.ImageField()
    description = models.TextField()
    type = models.ForeignKey('Type', related_name='Type', on_delete=models.CASCADE)

    def __str__(self):
        return f'Room - {self.number}'


class Type(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
