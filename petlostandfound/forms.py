from django import forms
from .models import LostPetReport, Pet

class LostPetReportForm(forms.ModelForm):
    pet_type = forms.ChoiceField(choices=Pet.PET_TYPE_CHOICES)
    name = forms.CharField(max_length=100, required=False)
    age = forms.IntegerField(required=False)
    breed = forms.CharField(max_length=50, required=False)
    sex = forms.ChoiceField(choices=Pet.GENDER_CHOICES, required=False)
    color = forms.CharField(max_length=50, required=False)
    
    class Meta:
        model = LostPetReport
        fields = ['reported_by', 'pet_type', 'report_date', 'last_seen_location', 'description', 'name', 'age', 'breed', 'sex', 'color']
