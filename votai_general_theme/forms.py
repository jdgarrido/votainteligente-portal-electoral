# coding=utf-8
from django import forms


class PersonalDataForm(forms.Form):
    age = forms.IntegerField(label='Edad', required=False, initial=0)
    lema = forms.CharField(label=u'Lema de campaña', required=False, initial='')
    ocupacion = forms.CharField(label=u'Ocupación', required=False, initial='')
    experiencia = forms.CharField(label=u'Experiencia en Cargos públicos',
                                  widget=forms.Textarea(),
                                  max_length=4096,
                                  required=False,
                                  initial=''
                                  )
