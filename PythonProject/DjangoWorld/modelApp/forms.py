from django import forms
from .models import DailyExpenseTracker


class dailyForm(forms.ModelForm):
    class Meta:
        model = DailyExpenseTracker
        fields = '__all__'