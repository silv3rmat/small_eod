# Generated by Django 3.0.3 on 2020-02-17 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0006_auto_20200126_0711'),
        ('events', '0002_auto_20200109_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='case',
            field=models.ForeignKey(help_text='Case for this event.', on_delete=django.db.models.deletion.DO_NOTHING, to='cases.Case', verbose_name='Case'),
        ),
        migrations.AlterField(
            model_name='event',
            name='comment',
            field=models.CharField(help_text='Comment text.', max_length=256, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='event',
            name='data',
            field=models.DateTimeField(help_text='Date of event.', verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(help_text='Name of event.', max_length=256, verbose_name='Name'),
        ),
    ]
