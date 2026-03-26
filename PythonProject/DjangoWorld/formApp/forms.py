from django import forms

class sampleForm(forms.Form):
    userName= forms.CharField(min_length=5,max_length=20,required=True)
    password= forms.CharField(min_length=5,max_length=20,widget=forms.PasswordInput())
    email= forms.CharField(min_length=5,max_length=20,widget=forms.EmailInput())
    age=forms.IntegerField()
    currency=forms.DecimalField(max_digits=10,decimal_places=2)
    isAdmin=forms.BooleanField()
    gender=forms.ChoiceField(choices=[('male','male'),('female','female')])
    day=forms.ChoiceField(choices=[('Monday','Monday'),('Tuesday','Tuesday')])
    file=forms.FileField()
    image = forms.ImageField()
    description=forms.CharField(required=False)