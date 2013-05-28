# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Material.description'
        db.add_column(u'material_material', 'description',
                      self.gf('django.db.models.fields.TextField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Material.description'
        db.delete_column(u'material_material', 'description')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'material.ausleihe': {
            'Meta': {'object_name': 'Ausleihe', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'bemerkungen': ('django.db.models.fields.TextField', [], {}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['material.MaterialStueck']"}),
            'reservation_begin': ('django.db.models.fields.DateTimeField', [], {}),
            'reservation_end': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'material.basemodel': {
            'Meta': {'object_name': 'BaseModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notice': ('django.db.models.fields.TextField', [], {})
        },
        u'material.bestellungen': {
            'Meta': {'object_name': 'Bestellungen', '_ormbases': [u'material.BaseModel']},
            'auftrag': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'material_stueck': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['material.MaterialStueck']"}),
            'rechnung': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'material.bilder': {
            'Meta': {'object_name': 'Bilder', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'material.dokumente': {
            'Meta': {'object_name': 'Dokumente', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'material.lagerort': {
            'Meta': {'object_name': 'LagerOrt', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'material.material': {
            'Meta': {'object_name': 'Material', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'kategorie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['material.MaterialKategorie']"}),
            'lagerort': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['material.LagerOrt']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zustand': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'material.materialkategorie': {
            'Meta': {'object_name': 'MaterialKategorie', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'standard_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'material.materialstueck': {
            'Meta': {'object_name': 'MaterialStueck', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'lagerort': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['material.LagerOrt']"}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['material.Material']"}),
            'stueckzahl': ('django.db.models.fields.FloatField', [], {}),
            'zustand': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'material.reservierung': {
            'Meta': {'object_name': 'Reservierung', '_ormbases': [u'material.BaseModel']},
            u'basemodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['material.BaseModel']", 'unique': 'True', 'primary_key': 'True'}),
            'bemerkungen': ('django.db.models.fields.TextField', [], {}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['material.MaterialStueck']"}),
            'reservation_begin': ('django.db.models.fields.DateTimeField', [], {}),
            'reservation_end': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['material']