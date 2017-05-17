from django.conf.urls import url
from .views import SignUp, LogIn, ChangePassword
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^sign_up/$', csrf_exempt(SignUp.as_view())),
    url(r'^log_in/$', csrf_exempt(LogIn.as_view())),
    url(r'^change_password/$', csrf_exempt(ChangePassword.as_view()))
]
