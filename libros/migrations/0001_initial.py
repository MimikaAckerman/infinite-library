# Generated by Django 4.2.2 on 2023-06-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('autor', models.CharField(max_length=50)),
                 ('descripcion', models.CharField(max_length=250)),
                ('archivo_pdf', models.FileField(upload_to='pdfs/')),
                ('fecha_publicacion', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
