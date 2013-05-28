# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import TemplateResponseMixin
from django.views.generic.edit import BaseFormView
from material.models import Material, Bestellungen, Ausleihe, MaterialKategorie
from material.forms import MaterialForm, LagerortForm, KategorieForm, ReservierungForm, MaterialStueckForm, BestellungForm, MaterialUpdateForm


class MaterialListView(ListView):
    model = Material
    template_name = 'materiallist.html'

class AusleiheListView(ListView):
    model = Ausleihe
    template_name = 'material/ausleihelist.html'

class MaterialCreate(CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'form.html'

class MaterialEdit(UpdateView):
    model = Material
    form_class = MaterialUpdateForm
    template_name = 'form.html'

class MaterialStueckCreate(CreateView):
    model = Material
    form_class = MaterialStueckForm
    template_name = 'form.html'

class LagerortCreate(CreateView):
    model = Material
    form_class = LagerortForm
    template_name = 'form.html'

class KategorieCreate(CreateView):
    model = MaterialKategorie
    form_class = KategorieForm
    template_name = 'form.html'

class KategorieEdit(UpdateView):
    model = MaterialKategorie
    form_class = KategorieForm
    template_name = 'form.html'


class ReservierungCreate(CreateView):
    model = Material
    form_class = ReservierungForm
    template_name = 'form.html'

class BestellungCreate(CreateView):
    model = Bestellungen
    form_class = BestellungForm
    template_name = 'form_file.html'

class BestellungListView(ListView):
    model = Bestellungen

class BestellungEditView(UpdateView):
    model = Bestellungen
    form_class = BestellungForm
    template_name = 'form_file.html'
