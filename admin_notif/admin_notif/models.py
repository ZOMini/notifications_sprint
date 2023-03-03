from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from djongo.models import Model, ObjectIdField


class CreateUser(Model):
    _id = ObjectIdField(verbose_name='notif_id')
    user_id = models.CharField('user_id', max_length=255)
    username = models.CharField('username', max_length=255)
    email = models.CharField('email', max_length=255)
    status = models.BooleanField('status')

    def __str__(self):
        return str(self._id)

class LikeComment(Model):
    _id = ObjectIdField(verbose_name='notif_id')
    review_id = models.CharField('review_id', max_length=255, )
    like_rating = models.FloatField('like_rating',
                                    validators=[MinValueValidator(0),
                                                MaxValueValidator(10)])
    username = models.CharField('username', max_length=255)
    email = models.CharField('email', max_length=255)
    status = models.BooleanField('status')

    def __str__(self):
        return str(self._id)
