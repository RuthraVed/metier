from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Candidate


class CandidateCreationForm(UserCreationForm):
    class Meta:
        model = Candidate
        fields = (
            "avatar",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "gender",
            "email",
        )


class CandidateChangeForm(UserChangeForm):
    class Meta:
        model = Candidate
        fields = (
            "avatar",
            "first_name",
            "middle_name",
            "last_name",
            "date_of_birth",
            "gender",
            "email",
        )
