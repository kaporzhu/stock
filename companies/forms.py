# -*- coding: utf-8 -*-
from django import forms

from .models import PurchasedCompany


class PurchasedCompanyForm(forms.ModelForm):

    class Meta:
        model = PurchasedCompany
        exclude = ('highest_price', 'company',)

    def __init__(self, *args, **kwargs):
        super(PurchasedCompanyForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
