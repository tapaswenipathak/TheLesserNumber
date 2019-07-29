from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget= forms.TextInput(attrs = 
                {
                    "class": "form-control", 
                    "placeholder": "Name"
                }
            )
        )
    email = forms.EmailField(widget = forms.EmailInput(attrs = 
                {
                    "class": "form-control", 
                    "placeholder": "Email"
                }
            )
        )
    message = forms.CharField(widget = forms.Textarea(attrs = 
                {
                    "class": "form-control", 
                    "placeholder": "Message"
                }
            )
        )
