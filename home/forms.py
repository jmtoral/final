from django import forms
from .models import Input, States, STATES

# abc: we only need one form to select the states. This form is "conected" in home/display_table
class InputForm(forms.ModelForm):

    state = forms.ChoiceField(choices=STATES, required=True,
                              widget=forms.Select())

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    class Meta:

        model = Input
        fields = ['state']



class StatesForm(forms.ModelForm):

    attrs = {'class ' : 'form-nav-control',
             'onchange ' : 'this.form.submit()'}

    state = forms.ChoiceField(choices = STATES, required = True,
                              widget = forms.Select(attrs = attrs))
    class Meta:

        model = States
        fields = ['state']
