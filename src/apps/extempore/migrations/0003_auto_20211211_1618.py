# Generated by Django 3.2.9 on 2021-12-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extempore', '0002_xtmfundocentry_is_custom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xtmfundocentry',
            options={'ordering': ['id'], 'verbose_name': 'XTM Function', 'verbose_name_plural': 'XTM Functions'},
        ),
        migrations.AddField(
            model_name='xtmfundocentry',
            name='permalink',
            field=models.CharField(blank=True, help_text='Unique name to be used in the for this function', max_length=350, verbose_name='permalink'),
        ),
        migrations.AlterField(
            model_name='xtmfundocentry',
            name='url',
            field=models.CharField(blank=True, help_text='URL to the github page for this function', max_length=350, verbose_name='url'),
        ),
    ]
