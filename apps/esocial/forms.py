from django import forms

from .choices import STATUS_EVENTO_CADASTRADO
from .models import Eventos, Certificados, Arquivos
from constance import config

class EventosForm(forms.ModelForm):
    evento_json = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Eventos
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventosForm, self).__init__(*args, **kwargs)
        self.fields['tpamb'].disabled = True

        if self.instance.pk:
            self.fields['evento'].disabled = True
            self.fields['versao'].disabled = True
            self.fields['operacao'].disabled = True

        if self.instance.pk and not self.instance.is_aberto:
            for f in list(self.fields):
                self.fields[f].disabled = True


class CertificadosForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Certificados
        fields = '__all__'


class ArquivosForm(forms.ModelForm):
    class Meta:
        model = Arquivos
        fields = '__all__'
