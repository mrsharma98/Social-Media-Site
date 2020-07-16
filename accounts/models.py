from django.db import models
from django.contrib import auth
# in-built user authorization by djnago

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
# firstname, lastname, username, email and one more attritube
# are provided by the auth.models.User
# this will automatically provide a basic form to the user.

    def __str__(self):
        return "@{}".format(self.username)
