# Generated by Django 2.2.24 on 2023-12-30 21:12

from django.db import migrations


def define_new_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for obj in list(Flat.objects.all()):
        if obj.construction_year >= 2015:
            obj.new_building = True
        else:
            obj.new_building = False
        obj.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20231226_1955'),
    ]

    operations = [
        migrations.RunPython(define_new_building)
    ]
