from django import forms
from djongo import models
from djongo.models import Model, ObjectIdField


class CreateUser(Model):
    _id = ObjectIdField(verbose_name='notif_id')
    user_id = models.CharField('user_id', max_length=255)
    username = models.CharField('username', max_length=255)
    email = models.CharField('email', max_length=255)
    status = models.BooleanField('status', default=False)

    def __str__(self):
        return str(self._id)

class ReviewLike(Model):
    _id = ObjectIdField(verbose_name='notif_id')
    user_id = models.CharField('user_id', max_length=255)
    username = models.CharField('username', max_length=255, blank=True)
    email = models.CharField('email', max_length=255, blank=True)
    ready = models.BooleanField('ready', default=False)
    status = models.BooleanField('status', default=False)

    def __str__(self):
        return str(self._id)

class User_obj(Model):
    user_id = models.CharField(max_length=255)

    class Meta:
        abstract = True
      
    def __str__(self):
        return self.user_id

class UserForm(forms.ModelForm):
    class Meta:
        model = User_obj
        fields = '__all__'

class AdminEvent(Model):
    _id = ObjectIdField(verbose_name='notif_id')
    ready = models.BooleanField('ready', default=False)
    status = models.BooleanField('status', default=False)
    objects = models.DjongoManager()
    user_ids = models.ArrayField(model_container=User_obj, model_form_class=UserForm)
    def __str__(self):
        return str(self._id)
