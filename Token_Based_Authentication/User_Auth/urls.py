from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^signup/$", views.Signup.as_view(), name="register"),
    url(r"^login/$", views.Login.as_view(), name="login"),
    url(r"^profile/$", views.Profile.as_view(), name="view-profile"),
]