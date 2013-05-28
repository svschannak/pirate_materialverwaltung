from django.conf.urls import patterns, url

from material import views

urlpatterns = patterns('',
    url(r'^$', views.MaterialListView.as_view(), name='materialindex'),
    url(r'^material/erstellen/$', views.MaterialCreate.as_view(), name='materialnew'),
    url(r'^material/bearbeiten/(?P<pk>[\w-]+)$', views.MaterialEdit.as_view(), name='materialedit'),
    url(r'^materialstueck/erstellen/$', views.MaterialStueckCreate.as_view(), name='materialstuecknew'),
    url(r'^lagerort/erstellen$', views.LagerortCreate.as_view(), name='lagerortnew'),

    url(r'^kategorie/erstellen$', views.KategorieCreate.as_view(), name='kategorienew'),
    url(r'^kategorie/bearbeiten', views.KategorieEdit.as_view(), name='kategorieedit'),
    url(r'^reservierung/erstellen$', views.ReservierungCreate.as_view(), name='reservierungnew'),

    url(r'^bestellung/uebersicht', views.BestellungListView.as_view(), name='bestellungen'),
    url(r'^bestellung/erstellen$', views.BestellungCreate.as_view(), name='bestellungnew'),
    url(r'^bestellung/bearbeiten/(?P<pk>[\w-]+)$', views.BestellungEditView.as_view(), name='bestellungedit'),

    url(r'^ausleihe/uebersicht/$', views.AusleiheListView.as_view(), name='ausleiheuebersicht'),
)