import random
from django.forms import ModelForm
from material.models import Material, LagerOrt, MaterialKategorie, Reservierung, MaterialStueck, Bestellungen


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = {'created', 'notice', 'inventarnummer'}

    def save(self, commit=True):
        instance = super(MaterialForm, self).save(commit=False)
        instance.inventarnummer = "PP%s" % random.randint(10000, 99999)
        #hack for already given inventarnumbers
        try:
            nummer = MaterialStueck.objects.get(inventarnummer=instance.inventarnummer)
            instance.inventarnummer = "PP%s" % random.randint(10000, 99999)
        except:
            if commit:
                instance.save()
            return instance

class MaterialUpdateForm(ModelForm):
    class Meta:
        model = Material
        exclude = {'created', 'notice'}



class MaterialStueckForm(ModelForm):
    class Meta:
        model = MaterialStueck
        exclude = {'created', 'notice'}

class LagerortForm(ModelForm):
    class Meta:
        model = LagerOrt
        exclude = {'created', 'notice'}

class KategorieForm(ModelForm):
    class Meta:
        model = MaterialKategorie
        exclude = {'created', 'notice'}

class ReservierungForm(ModelForm):
    class Meta:
        model = Reservierung
        exclude = {'created', 'notice'}


class BestellungForm(ModelForm):
    class Meta:
        model = Bestellungen
        exclude = {'created', 'notice'}