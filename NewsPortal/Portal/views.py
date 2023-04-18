from django.shortcuts import render
from django.views import generic
from Portal import models as mod


class ListNews(generic.ListView):
    model = mod.Post
    ordering = '-date_in'
    template_name = 'portal/ListNews.html'
    context_object_name = 'ListNews'


class DetailNews(generic.DetailView):
    model = mod.Post
    context_object_name = 'DetailNews'
    template_name = 'portal/DetailNews.html'


class CreateNews(generic.CreateView):  # FIXME
    model = mod.Post
    template_name = 'portal/CreateNews.html'
    context_object_name = 'CreatePost'


class UpdateNews(generic.CreateView):  # FIXME
    model = mod.Post
    template_name = 'portal/UpdateNews.html'
    context_object_name = 'UpdateNews'


class DeleteNews(generic.DeleteView): # FIXME
    model = mod.Post
    template_name = 'post/DeleteNews.html'
    context_object_name = 'DeleteNews'
