# Post views.py

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from djang.core.urlresolvers import reverse_lazy

from django.http import Http404
from django.views import generic
# Create your views here.

from braces.views import SelectRelatedMixin

from . import models
from . import forms

from django.contrib.auth import get_user_modoel
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):
    model = models.Post()
    select_related = ('user', 'group')
    # just a mixin that allows us to provide a tuple of th related model
    # basically the foreign keys for that post
    # user -> the post belongs to
    # group -> the post belongs to.


class UserPosts(generic.Listview):
    model = models.Post
    template_name = 'posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
            # basically when we call the user_post_list_view
            # it will attempt to try self.post.user i.e the user who belongs to that particular post
            # equal to user that user's object we are gin to prefetch related post
            # then the username should be exactly equal to whatever user logged in or
            # whatever user we clicked on.

        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

        # basically when we call the queryset for the user's post
        # that the user actually exist then we will be able to
        # fetch the post related to that user
        # using 'username__iexact=self.kwargs.get('username')'
        # and of the user doesnot exist then it will raise an exception
        # and raise Http404.


        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['post_user'] = self.post_user
            return context


class PostDetail(SelectRelatedMixin,generic.Detailview):
    model = models.Post
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        # getting the queryset for the actual post
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
        # the username we are passing has to be exactly the user's username.


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    fields = ('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = models.Post
    select_related = ('user', 'group')
    success_url = reverse_lazy('posts:all')

    def get_queryself(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args, **kwargs)
