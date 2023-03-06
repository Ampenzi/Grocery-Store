from django import forms 
from .models import ItemReviews

class ReviewForm(forms.ModelForm):
    review = forms.IntegerField()
    comment = forms.Textarea()

    class Meta:
        model = ItemReviews
        fields = ('review', 'comment')