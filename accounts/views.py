from django.views.generic import CreateView
from django.urls import reverse_lazy


from .forms import UserCreationForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "pages/registration/signup.html"
