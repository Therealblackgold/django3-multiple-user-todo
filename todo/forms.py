from django.forms import ModelForm
from .models import Todo
"""
Creating our own form, that will show in the browser for our users.
"""


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important']