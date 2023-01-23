


# from django import forms
# from .models import MyModel
# class MyModelForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ['custom_date']
#     def clean_custom_date(self):
#         date = self.cleaned_data['custom_date']
#         try:
#             datetime.strptime(date, '%d-%m-%Y')
#             return date
#         except ValueError:
#             raise forms.ValidationError("Incorrect format, should be DD-MM-YYYY")