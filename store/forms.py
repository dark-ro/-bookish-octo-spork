from django import forms

class ClientForm(forms.Form):
    email = forms.EmailField(
        label='email',
        max_length=200,
        required= True,
        widget = forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'} )
    )
    commentaire = forms.CharField(
        max_length=500,
        required=True,
        widget = forms.Textarea(attrs={'class': 'form-input2'})

    )
        