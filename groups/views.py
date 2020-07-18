from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

from django.core.urlresolvers import reverse
from django.views import generic
from groups.models import Group,GroupMember

# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroup(generic.ListView):
    model = Group

class JoinGroup(Logi, generic.RedirectView):

    # for sending the user to the newly joined group
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})


    def get(self, request, *args, **kwargs):
        # getting the group
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))
        try:
            #  trying to create a request to join the group
            GroupMember.object.create(user=self.request.user, group=group)

        #  if already a member
        except IntegrityError:
            messages.warning(self.request, ('Warning! Already a member'))

        # if user successfully joined the group
        else:
            messages.success(self.request, ('Yor are now the member!'))

        return super().get(request, *args, **kwargs)




class LeaveGroup(LoginRequiredMixin, generic.RedirectView):
    # for sending the user to the newly joined group
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug': self.kwargs.get('slug')})


    def get(self, request, *args, **kwargs):

        #  trying to get a membership, by assumming that the user is already in the group
        try:
            membership = models.GroupMember.objects.filter(
                user = self.request.user,
                group_slug = self.kwargs.get('slug')
            ).get()

        except models.GroupMember.DoesNotExist:
            messages.warning(self.request=, 'Sorry you aren\'t in this group!')

        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')

        return super().get(request, *args, **kwargs)
