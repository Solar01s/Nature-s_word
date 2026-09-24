from django import forms

'''
message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control', 
            'placeholder': 'Введите ваше сообщение...',
            'rows': 5
        })
    )
'''

class NewUserForm(forms.Form):
    username = forms.CharField(
        label='Your Real Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your name'})
    )
    email = forms.EmailField(
        label='Your Email',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'your-email@example.any'})
    )
    password = forms.CharField(label='Password',
                               max_length=100,
                               widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
                               )
    password2 = forms.CharField(label='Repeat Password',
                                max_length=100,
                                widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repeat Password'})
                                )
    age = forms.IntegerField(label='Age',
                             min_value=0,
                             max_value=100,
                             widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter your age'})
                             )
    about = forms.CharField(label='About',widget=forms.Textarea(attrs={'rows': 4}), max_length=500)

