from django.db import models
from django.views.generic.list import ListView
from django.contrib.auth.models import User
class main(ListView):
    template_name = "main.html"
    model = User
    context_object_name = "data"