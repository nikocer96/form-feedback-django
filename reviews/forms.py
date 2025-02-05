from django import forms

class ReviewForm(forms.Form):
    username_form = forms.CharField(label="Your Name", max_length=10)
    review_text = forms.CharField(label="Your Text", widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating", min_value=1, max_value=5)