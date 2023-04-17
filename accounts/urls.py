from django.urls import path
from .views import HomePageView, SignupPageView, TodoCreateView, TodoDeleteView, TodoDetailView, TodoUpdateView#, ProfilePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("signup/", SignupPageView.as_view(), name="signup"),
    path("create/", TodoCreateView.as_view(), name="create"),
    path("detail/<int:pk>", TodoDetailView.as_view(), name="detail"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="delete")
    # path("profile/", ProfilePageView.as_view(), name="profile"),
]