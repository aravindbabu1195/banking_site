import re
from django import forms
from .models import District, Branch, Registration, Material

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
       
        widgets = {
            # 'name':forms.TextInput(attrs={'class':'form-control'}),
            # 'date_of_birth':forms.DateInput(attrs={'class':'form-control'}),
            # 'age':forms.TextInput(attrs={'class':'form-control'}),
            # 'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
            # 'email':forms.TextInput(attrs={'class':'form-control'}),
            # 'address':forms.TextInput(attrs={'class':'form-control'}),
            'gender': forms.RadioSelect,
            'materials_provide': forms.CheckboxSelectMultiple,
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name should not contain numbers.")
        return name
    
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("Please enter a positive age.")
        if age < 18:
            raise forms.ValidationError("You must be 18 years or older to register.")
        if len(str(age)) > 2:
            raise forms.ValidationError("Please enter a valid two-digit age.")
        return age
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        phone_number_str = str(phone_number)
        if not phone_number_str.isdigit():
            raise forms.ValidationError("Please enter a valid phone number with digits only.")
        if int(phone_number_str) < 0:
            raise forms.ValidationError("Please enter a positive phone number.")
        if len(phone_number_str) != 10:
            raise forms.ValidationError("Phone number should be exactly 10 digits.")
        if not re.match(r'^[6-9]', phone_number_str):
            raise forms.ValidationError("Phone number should start with 6, 7, 8, or 9.")
        return phone_number

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set
        
        self.fields['name'].widget.attrs.update({
            'required':'',
            'name':'name',
            'id':'id_name',
            'type':'text',
            'class':'form-text',
            'placeholder':'Enter Name',
            'maxlength':'16',
            'minlength':'6',            
        })
        self.fields['date_of_birth'].widget.attrs.update({
            'required':'',
            'name':'date_of_birth',
            'id':'id_date_of_birth',
            'class':'form-text',
            'placeholder':'',
            'maxlength':'11',           
        })
        self.fields['age'].widget.attrs.update({
            'required':'',
            'name':'age',
            'id':'id_age',
            'type':'number',
            'class':'form-text',
            'placeholder':'Enter Age',
            'maxlength':'2',           
        })
        self.fields['email'].widget.attrs.update({
            'required':'',
            'name':'email',
            'id':'id_email',
            'type':'email',
            'class':'form-text',
            'placeholder':'Enter Email',
            'maxlength':'26',
            'minlength':'6',            
        })
        self.fields['phone_number'].widget.attrs.update({
            'required':'',
            'name':'phone_number',
            'id':'id_phone_number',
            'type':'number',
            'class':'form-text',
            'placeholder':'Enter Phone Number',
            'maxlength':'10',
            'minlength':'10',            
        })
        self.fields['address'].widget.attrs.update({
            'required':'',
            'name':'address',
            'id':'id_address',
            'type':'text',
            'class':'form-text',
            'placeholder':'Enter Address',
            'maxlength':'800',
            'minlength':'6',            
        })
        self.fields['district'].widget.attrs.update({
            'required':'',
            'name':'district',
            'id':'id_district',
            'type':'text',
            'class':'form-text',          
        })
        self.fields['branch'].widget.attrs.update({
            'required':'',
            'name':'branch',
            'id':'id_branch',
            'type':'text',
            'class':'form-text',           
        })
        self.fields['account_type'].widget.attrs.update({
            'required':'',
            'name':'account_type',
            'id':'id_account_type',
            'type':'text',
            'class':'form-text',            
        })
        self.fields['materials_provide'].widget.attrs.update({
            'name':'materials_provide',
            'id':'id_materials_provide',
            'type':'checkbox',
            'class':'form-text',
        })
class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name']

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'district']
