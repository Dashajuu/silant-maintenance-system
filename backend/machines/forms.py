from django import forms

from . import models


# factory function that generates a form class for Reference items' models
def make_reference_item_form(model_class):
    class ReferenceForm(forms.ModelForm):
        class Meta:
            model = model_class
            fields = ['name', 'description']

    return ReferenceForm


class MachineCreationForm(forms.ModelForm):
    class Meta:
        model = models.Machine
        fields = '__all__'
