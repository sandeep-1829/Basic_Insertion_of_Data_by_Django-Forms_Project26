from django import forms

g=[['MALE','MALE'],['FEMALE','FEMALE']]

c=[['PYTHON','PYTHON'],['DJANGO','DJANGO'],['SQL','SQL']]

class NameForm(forms.Form):
    Sname=forms.CharField()
    Sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':10}))
    # gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    # course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)