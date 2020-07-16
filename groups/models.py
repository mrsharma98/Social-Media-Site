from django.db import models
from django.utils.text import slugify
# basically slugify removes the alpha numeric values like space hyphen
# Eg if we have a string and we want ot use it as a url then
# this will replace spaces with underscore and so on.


# Groups models.py file
# Create your models here.
import misaka
#A Django template tag for rendering Markdown
from django.contrib.auth import get_user_model
# this returns user model tht is currently active in this project
User = get_user_model()
# creating a object of it.
# it allows to call things off of the current user's session.

from django import template
register = template.Library()


class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')\


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('group:single', kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')
    # User = get_user_model() -> allows us to link this with User

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')
