from django import forms

class Submission(forms.Form):
    name = forms.CharField(required=True,)
    manufacturer = forms.CharField(required=True)
    model = forms.CharField(required=True)
    img1 = forms.ImageField(required=False)
    img2 = forms.ImageField(required=False)
    img3 = forms.ImageField(required=False)

    def clean_name(self):
        if not self.name:
            raise forms.ValidationError('No name given')
        return self.name

    def clean_manufacturer(self):
        if not self.manufacturer:
            raise forms.ValidationError('No manufacturer given')
        return self.manufacturer
    
    def clean_model(self):
        if not self.model:
            raise forms.ValidationError('No model given')
        return self.model