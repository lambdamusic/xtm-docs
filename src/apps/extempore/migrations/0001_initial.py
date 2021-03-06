# Generated by Django 2.2.10 on 2021-01-22 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='XTMFundocEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time this record was firstly created. Do not modify.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Automatically updated each time the record is saved.')),
                ('editedrecord', models.BooleanField(default=False, help_text='Tick to indicate that this record has been finalized', verbose_name='edited record?')),
                ('review', models.BooleanField(default=False, help_text='Tick to indicate that this record is under review by the editorial team', verbose_name='review')),
                ('internal_notes', models.TextField(blank=True, verbose_name='internal_notes')),
                ('isprivate', models.BooleanField(blank=True, default=False, verbose_name='is private')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='name')),
                ('url', models.CharField(blank=True, max_length=350, verbose_name='url')),
                ('source', models.TextField(blank=True, verbose_name='implementation')),
                ('fungroup', models.CharField(blank=True, max_length=350, verbose_name='group eg by prefix normally')),
                ('funtype', models.CharField(blank=True, max_length=350, verbose_name='type eg whether r a macro or scheme function or xtlang')),
                ('desc', models.TextField(blank=True, verbose_name='desc')),
                ('signature', models.CharField(blank=True, max_length=300, verbose_name='signature')),
                ('examples', models.TextField(blank=True, verbose_name='examples')),
                ('args', models.TextField(blank=True, verbose_name='args')),
                ('returns', models.CharField(blank=True, max_length=300, verbose_name='returns')),
                ('related', models.CharField(blank=True, max_length=300, verbose_name='related')),
                ('created_by', models.ForeignKey(blank=True, help_text='No need to edit: automatically set when saving', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='created_xtmfundocentry', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, help_text='No need to edit: automatically set when saving', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='updated_xtmfundocentry', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'XTMFundocEntry',
                'verbose_name_plural': 'XTMFundocEntry',
                'ordering': ['id'],
            },
        ),
    ]
