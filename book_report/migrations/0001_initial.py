# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Publication'
        db.create_table('book_report_publication', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('edition', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('key_words', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('book_report', ['Publication'])

        # Adding model 'Summary'
        db.create_table('book_report_summary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('publication', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['book_report.Publication'])),
        ))
        db.send_create_signal('book_report', ['Summary'])


    def backwards(self, orm):
        
        # Deleting model 'Publication'
        db.delete_table('book_report_publication')

        # Deleting model 'Summary'
        db.delete_table('book_report_summary')


    models = {
        'book_report.publication': {
            'Meta': {'object_name': 'Publication'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_words': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'book_report.summary': {
            'Meta': {'object_name': 'Summary'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['book_report.Publication']"})
        }
    }

    complete_apps = ['book_report']
