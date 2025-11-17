from django import forms
from .models import CustomUser  # or Book if you have a Book model

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)

# Example using a model form
class BookForm(forms.ModelForm):
    class Meta:
        model = CustomUser  # Replace with your actual model if needed
        fields = ['username', 'email']  # or relevant fields
