# Generated by Django 4.2.4 on 2023-08-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aposentados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mci', models.CharField(max_length=9)),
                ('beneficio', models.CharField(max_length=255)),
                ('tipo_beneficio', models.CharField(max_length=1)),
                ('idade', models.CharField(max_length=3)),
                ('alfabetizado', models.CharField(max_length=1)),
                ('agencia', models.CharField(blank=True, max_length=5)),
                ('conta', models.CharField(blank=True, max_length=10)),
                ('dia_recebimento', models.CharField(max_length=2)),
                ('limite_vigente', models.CharField(max_length=1)),
                ('precisa_prova_vida', models.CharField(max_length=1)),
                ('ultimo_atendimento', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
