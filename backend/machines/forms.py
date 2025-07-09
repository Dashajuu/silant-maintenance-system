from django import forms

from . import models


def make_reference_item_form(model_class):
    class ReferenceForm(forms.ModelForm):
        class Meta:
            model = model_class
            fields = ['name', 'description']

    return ReferenceForm
