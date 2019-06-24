from django import forms

from .models import Filme

class FilmeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['year'].widget.attrs.update({'type': 'date'})

    class Meta:
        model = Filme
        fields = '__all__'