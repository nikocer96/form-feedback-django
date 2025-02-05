from django import forms
from .models import Review

# class ReviewForm(forms.Form):
#     username_form = forms.CharField(label="Your Name", max_length=10)
#     review_text = forms.CharField(label="Your Text", widget=forms.Textarea)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)


# QUESTO E' LO STESSO DI QUELLO DI SOPRA, MA PRENDE I CAMPI DIRETTAMENTE DAL MODELS(DB)
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            "username_form": "Your Name",
            "review_text": "Your Text",
            "rating": "Rating"
        }
        error_messages = {
            "username_form": {
                "required": "Il nome è obbligatorio"
            }
        }