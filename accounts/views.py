from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"

    def get_success_url(self):
        return reverse_lazy("login")
