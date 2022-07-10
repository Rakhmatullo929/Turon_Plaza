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


class Slide(BaseModel):
    image = models.ImageField(default='slide.jpg')

#
# class RoomPlaza(BaseModel):
#     image = models.ImageField()
#     type = models.ForeignKey('Type', related_name='Type', on_delete=models.CASCADE)
#     bathroom = models.CharField(null=True, max_length=50)
#     bedroom = models.CharField(null=True, max_length=50)
#     people = models.CharField(null=True, max_length=50)
#     price = models.IntegerField()
#
#     def __str__(self):
#         return f'{self.type}{self.people}'

#
# class Type(BaseModel):
#     title = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.title
