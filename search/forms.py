from django import forms
from .models import SearchQuery


class SearchQueryModelForm(forms.ModelForm):
    class Meta:
        model = SearchQuery
        fields = ['query']
