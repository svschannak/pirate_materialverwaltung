from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from material.views import KategorieEdit


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    notice = models.TextField()


MATERIAL_CHOICES = {
    ('WM', 'Wiederverwendbares Material'),
    ('GA', 'Give-Away'),
}

MATERIAL_ZUSTAND = {
    ('LEIH', 'Ausgeliehen'),
    ('RES', 'Reserviert'),
    ('AUS', 'Ausgesondert'),
    ('LAG', 'Eingelagert'),
}


class LagerOrt(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __unicode__(self):
        if self.name:
            return u'%s' % self.name


class MaterialKategorie(BaseModel):
    name = models.CharField(max_length=255)
    standard_type = models.CharField(max_length=255, choices=MATERIAL_CHOICES)

    def __unicode__(self):
        if self.name:
            return u'%s' % self.name

class Material(BaseModel):
    name = models.CharField(max_length=255)
    typ = models.CharField(max_length=255, choices=MATERIAL_CHOICES)
    zustand = models.CharField(max_length=255, choices=MATERIAL_ZUSTAND)
    kategorie = models.ForeignKey(MaterialKategorie)
    lagerort = models.ForeignKey(LagerOrt)
    description = models.TextField(blank=True)

    def __unicode__(self):
        if self.name:
            return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('materialedit', kwargs={'pk':self.id})

class MaterialStueck(BaseModel):
    material = models.ForeignKey(Material, related_name="material_stueck")
    stueckzahl = models.FloatField()
    zustand = models.CharField(max_length=255, choices=MATERIAL_ZUSTAND)
    lagerort = models.ForeignKey(LagerOrt)
    inventarnummer = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u'%s ( %s St. )' % (self.material.name, self.stueckzahl)


class Reservierung(BaseModel):
    material = models.ForeignKey(MaterialStueck)
    user = models.ForeignKey(User)
    reservation_begin = models.DateTimeField()
    reservation_end = models.DateTimeField()
    bemerkungen = models.TextField()

    def __unicode__(self):
        return u'%s' % self.material.name


class Ausleihe(BaseModel):
    material = models.ForeignKey(MaterialStueck)
    user = models.ForeignKey(User)
    beginn = models.DateTimeField(default=datetime.now())
    ende = models.DateTimeField(default=datetime.now())
    bemerkungen = models.TextField()

    def __unicode__(self):
        return u'%s' % self.material.name


BESTELLUNGEN_TYPEN = {
    ('1B', 'Erstbestellung'),
    ('NB', 'Nachbestellung'),
}

BESTELLUNGEN_STATUS = {
    ('BE', 'Bestellt'),
    ('SO', 'Soll bestellt werden'),
    ('AA', 'Angebot angefordert'),
    ('AE', 'Angebot erhalten'),
    ('LI', 'Wird geliefert'),
    ('AN', 'Lieferung angenommen'),
    ('AN', 'Inventarisiert'),
}

class Bestellungen(BaseModel):
    material_stueck = models.ForeignKey(MaterialStueck)
    typ = models.CharField(max_length=255, choices=BESTELLUNGEN_TYPEN)
    status = models.CharField(max_length=255, choices=BESTELLUNGEN_STATUS)
    rechnung = models.FileField(upload_to="rechnungen")
    auftrag = models.FileField(upload_to="rechnungen")
    link = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.material_stueck.material.name


class Dokumente(BaseModel):
    file = models.FileField(upload_to="dokumente")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')


class Bilder(BaseModel):
    file = models.ImageField(upload_to="bilder")
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')




