from django import forms




class Complain(forms.Form):
    Name=forms.CharField(required=True)
    Gmail=forms.EmailField(required=True)
    mobile=forms.IntegerField(required=True)
    complain=forms.CharField(widget=forms.Textarea ,required=True)
    url=forms.URLField()
    

