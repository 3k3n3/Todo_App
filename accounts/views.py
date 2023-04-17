from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CustomUserCreationForm
from .models import CustomUser, Todo

class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


# class ProfilePageView(TemplateView):
    # template_name = "accounts/profile.html"


class HomePageView(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = "todo"
    template_name = "accounts/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo"] = context["todo"].filter(user=self.request.user)
        return context


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ["title", "detail", "status"]
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TodoCreateView, self).form_valid(form)


class TodoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Todo
    # fields = ["title", "detail", "status"]

    def test_func(self):
        todo = self.get_object()
        return self.request.user == todo.user


class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ["title", "detail", "status"]
    success_url =  reverse_lazy("home")

    def test_func(self):
        todo = self.get_object()
        return self.request.user == todo.user


class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy("home")

    def test_func(self):
        todo = self.get_object()
        return self.request.user == todo.user
