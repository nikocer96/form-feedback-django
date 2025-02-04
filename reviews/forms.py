from django import forms

class ReviewForm(forms.Form):
    username_form = forms.CharField(label="Your Name", max_length=10)