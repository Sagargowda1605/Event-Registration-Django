from .models import Submission
from django.forms import ModelForm

class submission_form(ModelForm):
    class Meta:
        model=Submission
        fields=['title','details']