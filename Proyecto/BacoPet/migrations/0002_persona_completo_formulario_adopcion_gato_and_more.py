# Generated by Django 5.0.4 on 2024-04-21 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("BacoPet", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="persona",
            name="completo_formulario_adopcion_gato",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="persona",
            name="completo_formulario_adopcion_perro",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="persona",
            name="completo_formulario_patrocinador",
            field=models.BooleanField(default=False),
        ),
    ]