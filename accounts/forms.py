from django.contrib.auth import get_user_model
# this returns the user model that is currently active in this project.

from django.contrib.auth.forms import UserCreationForm
# there is already a user creation form build-in in the django.

class UserCreateForm(UserCreationForm):

    class Meta():
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()
        # this allows us to get the current model.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Address'

    # When the user comes in and ready to sign up
    # we are going to call UserCreationForm from auth.forms
    # then we set up a Meta class and provide the particular
    # fields to user to fill them when they are signing up
    # so whenever we connect models to database these are the
    # fields we will have access to
    # now if we actually want the labels on that forms so
    # we can call the super() class
    # we will end up doing self.field['username'].label = 'label name of that field'
    # this is almost like a dictionary
    # thats the same thing setting up a label on form html page
    # but here we are setting from the actual forms.py view
    # this naming we do for our convinency
