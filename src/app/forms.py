from dataclasses import fields
from socket import fromshare
from django import forms
from app.models import *


class ProductionForm(forms.ModelForm):
    class Meta:
        model = production
        fields = [
            "codeprod",
            "qte",
            "dteprod",
            "qtedechet",
        ]
        