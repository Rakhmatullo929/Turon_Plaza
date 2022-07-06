from django.db import models


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Room(models.Model):
    number = models.IntegerField(null=True)
    image = models.ImageField()
    description = models.TextField()
    type = models.ForeignKey('hotel.Type', on_delete=models.CASCADE)

    def __str__(self):
        return f'Room - {self.number}'


class Type(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
