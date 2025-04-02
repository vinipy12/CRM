# Generated by Django 5.1.5 on 2025-01-30 01:15

import django.db.models.deletion
import files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('endereco', models.FileField(upload_to=files.models.file_upload_path)),
                ('data_upload', models.DateTimeField(editable=False)),
                ('ano', models.CharField(max_length=4)),
                ('validade', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='customers.empresa')),
            ],
        ),
    ]
