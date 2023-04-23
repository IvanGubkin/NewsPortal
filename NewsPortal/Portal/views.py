from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from Portal import models as mod
from .forms import CreateNewsForm
from .filters import PostListSearch
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class ListNews(generic.ListView):
    model = mod.Post
    ordering = '-date_in'
    template_name = 'portal/ListNews.html'
    context_object_name = 'ListNews'
    paginate_by = 2

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostListSearch(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class DetailNews(LoginRequiredMixin, generic.DetailView):
    model = mod.Post
    context_object_name = 'DetailNews'
    template_name = 'portal/DetailNews.html'


class CreateNews(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):  # FIXME
    model = mod.Post
    template_name = 'portal/CreateNews.html'
    context_object_name = 'CreatePost'
    form_class = CreateNewsForm
    success_url = reverse_lazy('ListNews')
    permission_required = ('Portal.add_post',)

    # Добавляем что бы автор добавлялся автоматечески
    def form_valid(self, form):
        form.instance.author = self.request.user.author
        return super().form_valid(form)


class UpdateNews(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):  # FIXME
    model = mod.Post
    form_class = CreateNewsForm
    template_name = 'portal/UpdateNews.html'
    context_object_name = 'UpdateNews'
    success_url = reverse_lazy('ListNews')
    permission_required = ('Portal.chenge_post')


class DeleteNews(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):  # FIXME
    model = mod.Post
    template_name = 'portal/DeleteNews.html'
    context_object_name = 'DeleteNews'
    success_url = reverse_lazy('ListNews')
    permission_required = ('Portal.delete_post')
